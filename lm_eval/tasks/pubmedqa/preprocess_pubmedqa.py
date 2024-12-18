def doc_to_text(doc) -> str:
    ctxs = "\n".join(doc["CONTEXTS"])

    meshes = "\n".join(doc["MESHES"])

    labels = "\n".join(doc["LABELS"])

    # abstract = ctxs + "\n MeSH:" + meshes + "\n Labels:" + labels

    abstract = "\n MeSHes: " + meshes + "\n Contexts: " + ctxs
    return "Abstract: {}\nQuestion: {}\nAnswer:".format(
        abstract,
        doc["QUESTION"],
    )
