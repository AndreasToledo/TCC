<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <title>Resultado da Redação</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 30px; }
        .nota { font-size: 1.5em; margin-bottom: 20px; }
        .feedback { background: #f7f7f7; border-radius: 8px; padding: 20px; margin-bottom: 20px; }
        .feedback h2 { margin-top: 0; }
        ul { padding-left: 20px; }
        .voltar { margin-top: 30px; }
    </style>
</head>
<body>
    <h1>Resultado da Redação</h1>
    <div class="nota">
        Nota: <strong>{{ e($nota) }}/1000</strong>
    </div>
    <div class="feedback">
        <h2>Feedbacks</h2>
        @if(isset($feedback['feedback']) && is_array($feedback['feedback']) && count($feedback['feedback']) > 0)
            <ul>
                @foreach($feedback['feedback'] as $item)
                    <li>{{ e($item) }}</li>
                @endforeach
            </ul>
        @else
            <p>Nenhum feedback gerado.</p>
        @endif
    </div>
    <div class="voltar">
        <a href="/">Voltar</a>
    </div>
</body>