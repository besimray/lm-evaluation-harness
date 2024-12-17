def doc_to_text(doc) -> str:
    ctxs = "\n".join(doc["CONTEXTS"])

    meshes = "\n".join(doc["MESH"])

    abstract = ctxs + "\n MeSH:" + meshes
    return "Abstract: {}\nQuestion: {}\nAnswer:".format(
        abstract,
        doc["QUESTION"],
    )
