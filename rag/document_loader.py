from pathlib import Path
from pypdf import PdfReader


class DocumentLoader:

    def load_pdf(self, file_path):

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:

            text += page.extract_text() or ""

        return text

    def load_text(self, file_path):

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            return f.read()

    def load_document(self, file_path):

        path = Path(file_path)

        suffix = path.suffix.lower()

        if suffix == ".pdf":
            return self.load_pdf(file_path)

        elif suffix in [".txt", ".md"]:
            return self.load_text(file_path)

        else:
            raise ValueError(
                f"Unsupported file type: {suffix}"
            )