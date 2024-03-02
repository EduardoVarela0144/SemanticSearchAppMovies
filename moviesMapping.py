moviesMapping = {
    "properties": {
        "title": {
            "type": "text"
        },
        "year": {
            "type": "integer"
        },
        "cast": {
            "type": "text"
        },
        "genres": {
            "type": "keyword"
        },
        "href": {
            "type": "keyword"
        },
        "extract": {
            "type": "text"
        },
        "thumbnail": {
            "type": "keyword"
        },
        "thumbnail_width": {
            "type": "integer"
        },
        "thumbnail_height": {
            "type": "integer"
        },
        "vector": {
            "type": "dense_vector",
            "dims": 768,
            "index": True,
            "similarity": "l2_norm"
        }
    }

}
