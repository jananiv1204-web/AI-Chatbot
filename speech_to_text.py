import tempfile


def save_audio(audio):

    if audio is None:
        return None

    temp_file = tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".wav"
    )

    temp_file.write(audio["bytes"])
    temp_file.close()

    return temp_file.name