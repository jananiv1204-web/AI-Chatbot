from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_text(text):
    """
    Split PDF text into overlapping chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=200,
        separators=["\n\n", "\n", ".", " ", ""]
    )

    chunks = splitter.split_text(text)

    return chunks