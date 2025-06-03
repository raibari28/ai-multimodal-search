# AI Multimodal Search & Document Research

A Streamlit app that lets you:
- Upload and read PDF, Word, Excel, PowerPoint, and image files
- Extracts and displays their content
- Uses OpenAI GPT to generate a research query from your document
- Cross-checks your content with live web results (Google search + web scraping)
- Summarizes and compares both sources

## Setup

1. Clone this repo.
2. `pip install -r requirements.txt`
3. `playwright install`
4. Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for image reading (Linux: `sudo apt install tesseract-ocr`).
5. Set your OpenAI API key:  
   - On Linux/Mac: `export OPENAI_API_KEY=sk-...`
   - On Windows: `set OPENAI_API_KEY=sk-...`
6. Run: `streamlit run app.py`

## Usage

- Upload a supported file.
- Click "Research & Cross-Check Online".
- See extracted text and a GPT-powered, evidence-based summary.

## Supported Files

- PDF, DOCX, XLSX, PPTX
- JPG, PNG (with OCR)

## Notes

- Only text is extracted from images and office documents (no formatting, formulas, or embedded objects).
- Cross-check is as good as the OpenAI model and web search allows.
