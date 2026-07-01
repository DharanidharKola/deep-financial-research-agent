from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from backend.rag.vector_store import (
    VECTOR_DB
)

DATA_PATH = "data"


def ingest_documents():

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500,
        chunk_overlap=100
    )

    pdf_files = list(
        Path(DATA_PATH).rglob("*.pdf")
    )

    print(f"Found {len(pdf_files)} PDFs")

    documents = []

    for pdf in pdf_files:

        print(f"Loading: {pdf.name}")

        loader = PyPDFLoader(
            str(pdf)
        )

        pages = loader.load()

        company_name = pdf.stem

        # Detect sector
        it_companies = [
            "Infosys",
            "TCS",
            "Wipro"
        ]

        if any(
            company in pdf.stem
            for company in it_companies
        ):
            sector = "IT"
        else:
            sector = "Pharma"

        chunks = splitter.split_documents(
            pages
        )

        # Add metadata to every chunk
        for chunk in chunks:

            chunk.metadata["company"] = (
                company_name
            )

            chunk.metadata["sector"] = (
                sector
            )

            chunk.metadata["source"] = (
                pdf.name
            )

        documents.extend(chunks)

    print(
        f"Total chunks created: {len(documents)}"
    )

    print(
        "Starting Pinecone upload..."
    )

    batch_size = 50

    for i in range(
        0,
        len(documents),
        batch_size
    ):

        batch = documents[
            i:i + batch_size
        ]

        VECTOR_DB.add_documents(
            batch
        )

        print(
            f"Uploaded "
            f"{min(i+batch_size, len(documents))}"
            f"/{len(documents)} chunks"
        )

    print("Upload complete!")


if __name__ == "__main__":

    ingest_documents()