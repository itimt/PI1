import cv2

nome_arquivo = 'nave.jpeg' 
imagem = cv2.imread(nome_arquivo)

if imagem is None:
    print("Erro: Arquivo de imagem não encontrado!")
else:
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Missao 4 - Teste Nativo', imagem_cinza)

    print("Pressione qualquer tecla na janela da imagem para fechar...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()