import os
import glob

# Defina o nome da pasta onde estão os arquivos de texto e o nome do arquivo de saída
pasta_origem = 'txt'
arquivo_saida = 'machado_de_assis_corpus.txt'

def concatenar_textos(pasta, saida):
    # Procura por todos os arquivos com extensão .txt dentro da pasta especificada
    caminho_busca = os.path.join(pasta, '*/*.txt')
    arquivos_txt = glob.glob(caminho_busca)
    
    # Ordena os arquivos alfabeticamente (opcional, mas bom para manter a organização)
    arquivos_txt.sort()
    
    if not arquivos_txt:
        print(f"Nenhum arquivo .txt foi encontrado na pasta '{pasta}'. Verifique o caminho.")
        return

    print(f"Encontrados {len(arquivos_txt)} arquivos. Iniciando a concatenação...")

    # Abre o arquivo de saída no modo de escrita ('w') usando UTF-8
    with open(saida, 'w', encoding='utf-8') as f_out:
        for caminho_arquivo in arquivos_txt:
            try:
                # Lê cada arquivo individualmente usando UTF-8
                with open(caminho_arquivo, 'r', encoding='utf-8') as f_in:
                    conteudo = f_in.read()
                    
                    # Escreve o conteúdo no arquivo final
                    f_out.write(conteudo)
                    
                    # Adiciona quebras de linha entre os livros/textos para evitar que 
                    # a última palavra de um grude na primeira palavra de outro
                    f_out.write('\n\n')
                    
            except Exception as e:
                print(f"Erro ao processar o arquivo {caminho_arquivo}: {e}")

    print(f"Sucesso! O corpus foi gerado e salvo como: {saida}")

if __name__ == '__main__':
    concatenar_textos(pasta_origem, arquivo_saida)