# CP1 - Visão Computacional com ESP32-CAM e YOLO

## Integrantes

| Nome | RM |
|---|---:|
| Lucas Bomtempo | 568585 |
| Caio Apolinario | 569268 |
| Arthur Lins | 570110 |
| Lucas Herrero | 570557 |

## 1. Objetivo

O projeto tem como objetivo desenvolver a etapa de construção de um dataset para um sistema de visão computacional utilizando uma ESP32-CAM e o modelo YOLO para detecção de objetos.

A ESP32-CAM é utilizada para realizar a captura das imagens. Após a coleta, as imagens são organizadas e anotadas no Roboflow, utilizando bounding boxes para identificar os objetos pertencentes às classes definidas no projeto.

O dataset produzido é posteriormente exportado em formato compatível com YOLO.

## 2. Tecnologias utilizadas

- ESP32-CAM AI Thinker
- MicroPython
- Python
- Roboflow
- YOLO
- YOLOv11 Nano

## 3. Classes do projeto

O dataset possui duas classes:

| Classe | Quantidade de imagens |
|---|---:|
| redbull can | 104 |
| caneca | 73 |

A quantidade de 73 imagens para a classe `caneca` foi autorizada pelo professor.

## 4. Coleta das imagens

As imagens utilizadas no projeto foram coletadas utilizando a ESP32-CAM.

Durante a construção do dataset, foram consideradas variações de ângulo, distância, iluminação, posição dos objetos e fundo, buscando evitar imagens excessivamente repetitivas.

Após a coleta, as imagens foram organizadas para serem utilizadas na etapa de anotação.

## 5. Anotação das imagens

As imagens foram enviadas para o Roboflow e anotadas utilizando bounding boxes.

Cada objeto identificado foi associado à sua respectiva classe:

- `redbull can`
- `caneca`

As bounding boxes foram posicionadas sobre os objetos presentes nas imagens para identificar sua localização e respectiva classe.

## 6. Roboflow

O dataset foi desenvolvido e organizado utilizando o Roboflow.

**Projeto:** `redbull-sklf8`

**Versão do dataset:** `v3`

**Link do projeto:**

https://app.roboflow.com/lucas-silverio-bomtempo-silverio-bomtempo/redbull-sklf8/browse

## 7. Organização do dataset

O dataset foi exportado em formato compatível com YOLO.

A estrutura contém os diretórios de treinamento, validação e teste, além do arquivo `data.yaml`.

```text
dataset/
├── data.yaml
├── train/
│   ├── images/
│   └── labels/
├── valid/
│   ├── images/
│   └── labels/
└── test/
    ├── images/
    └── labels/

## 8. Firmware

O firmware da ESP32-CAM foi desenvolvido utilizando MicroPython.

Os arquivos do firmware estão localizados na pasta `firmware/`.

```text
firmware/
├── boot.py
└── main.py
```

O firmware permite a conexão da ESP32-CAM à rede Wi-Fi e disponibiliza um servidor HTTP para acesso à câmera através do navegador, possibilitando a visualização e captura das imagens.

## 9. Treinamento e testes

Foi realizado um treinamento experimental utilizando o modelo YOLOv11 Nano com o dataset desenvolvido.

Também foram realizados testes de detecção utilizando as classes `redbull can` e `caneca`.

## 10. Evidências

As evidências do desenvolvimento do projeto estão disponíveis na pasta `evidencias/`.

Entre as evidências estão:

- ESP32-CAM funcionando;
- Visualização da câmera através do navegador;
- Dataset no Roboflow;
- Organização e versão do dataset;
- Anotações das classes;
- Treinamento experimental;
- Testes de detecção.

## 11. Estrutura da entrega

A estrutura final do projeto está organizada da seguinte maneira:

```text
CP1/
├── firmware/
│   ├── boot.py
│   └── main.py
│
├── evidencias/
│   ├── esp32cam_funcionando.png
│   └── Roboflow_CP1_Documentacao.pdf
│
├── dataset/
│   └── redbull.v3i.yolov11.zip
│
└── README.md
```

## 12. Execução da ESP32-CAM

Para executar o firmware:

1. Configurar o ambiente MicroPython para a ESP32-CAM AI Thinker.
2. Configurar as informações da rede Wi-Fi no código.
3. Enviar os arquivos do firmware para a ESP32-CAM.
4. Executar o programa na placa.
5. Identificar o endereço IP disponibilizado pela ESP32-CAM.
6. Acessar o endereço IP através de um navegador.
7. Utilizar a interface web para visualizar e realizar capturas de imagens.

## 13. Resultado

Ao final do processo, foi desenvolvido um dataset com duas classes de objetos, contendo imagens coletadas, organizadas e anotadas no Roboflow.

O dataset foi exportado em formato YOLO e utilizado experimentalmente para o treinamento de um modelo YOLOv11 Nano e realização de testes de detecção.

As evidências e os arquivos utilizados no desenvolvimento estão organizados nas respectivas pastas desta entrega.
