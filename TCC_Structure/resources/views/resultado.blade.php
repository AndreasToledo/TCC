<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <title>Resultado da Redação</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f4f4;
        }

        h1 {
            color: #333;
        }

        .container {
            background-color: #fff;
            border-radius: 10px;
            padding: 30px;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
            max-width: 700px;
            margin: auto;
        }

        .nota {
            font-size: 1.8em;
            margin-bottom: 20px;
            color: #2c3e50;
        }

        .feedback h2 {
            margin-top: 0;
            font-size: 1.4em;
            color: #444;
        }

        .feedback ul {
            list-style: disc;
            padding-left: 25px;
            line-height: 1.6;
        }

        .feedback {
            background: #fdfdfd;
            border-left: 4px solid #3498db;
            border-radius: 5px;
            padding: 20px;
            margin-bottom: 30px;
        }

        .voltar {
            text-align: center;
            margin-top: 30px;
        }

        .voltar a {
            text-decoration: none;
            color: #3498db;
            font-weight: bold;
        }

        .voltar a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Resultado da Redação</h1>

        <div class="nota">
            Nota: <strong>{{ e($nota) }}/1000</strong>
        </div>

        <div class="feedback">
            <h2>Feedbacks</h2>
            @if(isset($feedback['feedback']) && is_array($feedback['feedback']) && count($feedback['feedback']) > 0)
                <ul>
                    @foreach($feedback['feedback'] as $item)
                        @php
                            $partes = explode(':', $item, 2);
                            $titulo = trim($partes[0] ?? '');
                            $mensagem = trim($partes[1] ?? '');
                        @endphp

                        <li>
                            <strong>{{ $titulo }}</strong>: {{ $mensagem }}
                        </li>
                    @endforeach
                </ul>
            @else
                <p>Nenhum feedback gerado.</p>
            @endif
        </div>

        <div class="voltar">
            <a href="/">← Voltar</a>
        </div>
    </div>
</body>
</html>
