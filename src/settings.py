DOMAIN_DESCRIPTIONS = {
    "netflix_titles": {
        "schema": "netflix_refined",
        "table": "tb_glue_api_netflix_titles_refined",
        "columns": {
            "show_id": "Identificador único para cada título (s1, s2).",
            "type": "Especifica se o título é um 'Filme' ou 'Série'.",
            "title": "O nome do título na Netflix.",
            "director": "O diretor do título.",
            "movie_cast": "Os principais atores envolvidos no título.",
            "country": "O país onde o título foi produzido.",
            "date_added": "A data em que o título foi adicionado à Netflix.",
            "release_year": "O ano em que o título foi originalmente lançado.",
            "rating": "A classificação de conteúdo ('PG-13', 'TV-MA').",
            "duration": "Duração do filme (em minutos) ou o número de temporadas para séries.",
            "listed_in": "Categorias ou gêneros em que o título se enquadra ('Documentários', 'Dramas de TV').",
            "description": "A descrição resumida do título.",
        },
    },
}
