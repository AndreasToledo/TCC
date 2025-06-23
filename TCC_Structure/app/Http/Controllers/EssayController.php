<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class EssayController extends Controller
{    
    public function resultado(Request $request){
        $texto = $request->input('texto');

        // 1. Gera a nota
        $processNota = proc_open(
            'python ..\..\IA_TCC\inferencia.py',
            [
                0 => ['pipe', 'r'],
                1 => ['pipe', 'w'],
                2 => ['pipe', 'w'] 
            ],
            $pipesNota
        );

        $nota = null;
        $notaError = null;
        $notaReturn = null;

        if (is_resource($processNota)) {
            fwrite($pipesNota[0], $texto);
            fclose($pipesNota[0]);

            $nota = stream_get_contents($pipesNota[1]);
            fclose($pipesNota[1]);

            $notaError = stream_get_contents($pipesNota[2]);
            fclose($pipesNota[2]);

            $notaReturn = proc_close($processNota);

            $nota = mb_convert_encoding($nota, 'UTF-8', 'UTF-8');
            $nota = trim($nota);
        }

        // 2. Gera o feedback
        $processFeedback = proc_open(
            'python ..\..\IA_analise\main.py',
            [
                0 => ['pipe', 'r'],
                1 => ['pipe', 'w'],
                2 => ['pipe', 'w'] 
            ],
            $pipesFeedback
        );

        $feedback = null;
        $feedbackError = null;
        $feedbackReturn = null;

        if (is_resource($processFeedback)) {
            fwrite($pipesFeedback[0], $texto);
            fclose($pipesFeedback[0]);

            $feedback = stream_get_contents($pipesFeedback[1]);
            fclose($pipesFeedback[1]);

            $feedbackError = stream_get_contents($pipesFeedback[2]);
            fclose($pipesFeedback[2]);

            $feedbackReturn = proc_close($processFeedback);

            $feedback = mb_convert_encoding($feedback, 'UTF-8', 'UTF-8');
            $feedback = trim($feedback);
        }

        // 3. Verifica erros e retorna resposta JSON
        if ($notaReturn !== 0) {
            return response()->json(['erro' => 'Erro ao executar o script de nota: ' . $notaError], 500);
        }
        if ($feedbackReturn !== 0) {
            return response()->json(['erro' => 'Erro ao executar o script de feedback: ' . $feedbackError], 500);
        }

        // Decodifica o feedback JSON
        $feedbackDecoded = json_decode($feedback, true);

        if (!mb_check_encoding($nota, 'UTF-8') || !mb_check_encoding($feedback, 'UTF-8')) {
            return response()->json(['erro' => 'Saída inválida: encoding malformado'], 500);
        }

        return view('resultado', [
            'nota' => $nota,
            'feedback' => $feedbackDecoded
        ]);
    }
}