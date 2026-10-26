"""Cria notebooks de resolução sem alterar Markdown nem sobrescrever notebooks."""
import argparse
import json
import re
from pathlib import Path


def cell(kind, text):
    item = {'cell_type': kind, 'metadata': {}, 'source': text.splitlines(keepends=True)}
    if kind == 'code':
        item.update(execution_count=None, outputs=[])
    return item


def convert(root):
    files = sorted(root.glob('dia_*/enunciado_e_resposta.md'))
    if not files:
        raise SystemExit('Nenhum dia encontrado. Informe a pasta Planner_56_dias.')
    created = 0
    for source in files:
        destination = source.with_name('resolucao.ipynb')
        if destination.exists():
            print(f'Preservado: {destination}')
            continue
        try:
            text = source.read_text(encoding='utf-8-sig')
        except UnicodeDecodeError:
            raise SystemExit(f'{source}: codificação inválida; original preservado. Converta para UTF-8.')
        # Os caminhos do enunciado partem da pasta do planner. No notebook,
        # os dados estão ao lado do próprio arquivo.
        text = text.replace(source.parent.name + '/', './')
        text = re.split(r'\n\*\*Minha resposta / evidências:\*\*', text, maxsplit=1)[0]
        cells = [cell('markdown', text),
                 cell('markdown', '## Minha estratégia\n\nExplique como pretende abordar o problema.'),
                 cell('markdown', '## Resolução\n\nOs arquivos de dados estão nesta pasta. Se necessário, confira o diretório de execução com `Path.cwd()`. Acrescente células conforme precisares.'),
                 cell('code', ''),
                 cell('markdown', '## Resultados e interpretação\n\nResponda às perguntas do enunciado e explique os resultados.'),
                 cell('markdown', '## Conferência dos critérios\n\nRegistre as evidências de conclusão e as dúvidas que restaram.')]
        notebook = {'cells': cells, 'metadata': {'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}, 'language_info': {'name': 'python'}}, 'nbformat': 4, 'nbformat_minor': 4}
        # Modo exclusivo: nunca substitui uma resolução existente.
        with destination.open('x', encoding='utf-8') as stream:
            json.dump(notebook, stream, ensure_ascii=False, indent=2)
            stream.write('\n')
        print(f'Criado: {destination}')
        created += 1
    print(f'Concluído: {created} notebooks novos; {len(files)-created} preservados.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pasta', type=Path, help='Pasta Planner_56_dias com as subpastas dia_XX')
    convert(parser.parse_args().pasta.expanduser().resolve())
