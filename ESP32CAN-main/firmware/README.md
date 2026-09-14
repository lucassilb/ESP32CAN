# Firmware ESP32-CAM (MicroPython)

Firmware utilizado para configurar a ESP32-CAM (AI Thinker) e disponibilizar a captura de imagens via HTTP, usado na etapa de coleta do dataset.

## Arquivos

- `boot.py`: conecta a ESP32-CAM na rede Wi-Fi 2.4 GHz configurada.
- `main.py`: inicializa a câmera e sobe um servidor HTTP simples com duas rotas:
  - `/`: página HTML com visualização da imagem capturada.
  - `/capture`: retorna uma nova foto em JPEG a cada requisição.

## Configuração

1. Editar `WIFI_SSID` e `WIFI_PASSWORD` em `boot.py`.
2. Gravar `boot.py` e `main.py` na ESP32-CAM (AI Thinker) via `ampy`, `rshell`, Thonny ou ferramenta equivalente de upload MicroPython.
3. Reiniciar a placa e verificar no monitor serial o IP atribuído.
4. Acessar `http://<IP_DA_ESP32>/` no navegador para visualizar a câmera e `http://<IP_DA_ESP32>/capture` para obter uma imagem.

## Uso na coleta do dataset

As imagens obtidas em `/capture` foram salvas manualmente e renomeadas seguindo o padrão `classe_numero.jpg` (ex.: `redbull_001.jpg`, `caneca_001.jpg`), depois enviadas ao Roboflow para anotação.
