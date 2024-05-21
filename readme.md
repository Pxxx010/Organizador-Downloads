# File Organizer | Organizador-Downloads

Este script em Python organiza arquivos em pastas com base em suas extensões. Ele percorre as pastas especificadas e move os arquivos para subpastas correspondentes aos seus tipos. Arquivos que não correspondem a nenhum tipo predefinido são movidos para pastas com base em suas extensões.

## Funcionalidades

- Organiza arquivos de acordo com as seguintes categorias:
  - EXCEL: `XLSM`, `XLSX`, `XLS`, `CSV`, `XLAM`, `XLA`
  - FOTOS: `JPG`, `JPEG`, `PNG`, `GIF`, `SVG`, `BMP`
  - MUSIC: `MP3`, `WAV`, `FLAC`
  - VIDEO: `MP4`, `AVI`, `MOV`
  - PYTHON: `PY`, `PYTHON`, `IPYNB`
  - PDF: `PDF`
  - ZIP: `ZIP`, `RAR`, `7Z`
  - POWERPOINT: `PPT`, `PPTX`, `ODP`
  - TEXT: `TXT`
  - APPS: `EXE`
  - HTML: `HTML`
  - WORD: `DOC`, `DOCX`
  - SECURE: `CER`, `KEY`, `REN`, `REQ`
- Move arquivos para pastas apropriadas.
- Cria pastas novas conforme necessário.
- Remove pastas vazias após a organização.

## Como usar

1. Clone este repositório:
    ```bash
    git clone https://github.com/Pxxx010/Organizador-Downloads
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd organizador-python
    ```

3. Execute o script:
    ```bash
    python organizador-downloads.py
    ```

## Estrutura do Projeto

```plaintext
organizador-downloads/
├── organizador-downloads.py
└── README.md
