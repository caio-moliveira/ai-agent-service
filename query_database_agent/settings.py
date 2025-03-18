DOMAIN_DESCRIPTIONS = {
    "sales": {
        "schema": "public",
        "table": "my_sales",
        "columns": {
            "sale_id": {
                "description": "Identificador único da transação",
                "data_type": "TEXT",
            },
            "sale_date": {
                "description": "Data da venda",
                "data_type": "TEXT",
            },
            "product_id": {
                "description": "Identificador único do produto",
                "data_type": "TEXT",
            },
            "product_name": {
                "description": "Nome do produto",
                "data_type": "TEXT",
            },
            "product_category": {
                "description": "Categoria à qual o produto pertence",
                "data_type": "TEXT",
            },
            "quantity_sold": {
                "description": "Número de unidades vendidas",
                "data_type": "BIGINT",
            },
            "unit_price": {
                "description": "Preço por unidade",
                "data_type": "DOUBLE PRECISION",
            },
            "discount_percentage": {
                "description": "Desconto aplicado à venda",
                "data_type": "BIGINT",
            },
            "total_value": {
                "description": "Valor total da transação após descontos",
                "data_type": "DOUBLE PRECISION",
            },
            "unit_cost": {
                "description": "Custo por unidade para a empresa",
                "data_type": "DOUBLE PRECISION",
            },
            "total_cost": {
                "description": "Custo total da transação",
                "data_type": "DOUBLE PRECISION",
            },
            "gross_profit": {
                "description": "Lucro bruto após subtração dos custos",
                "data_type": "DOUBLE PRECISION",
            },
            "payment_method": {
                "description": "Forma de pagamento utilizada",
                "data_type": "TEXT",
            },
            "payment_status": {
                "description": "Status do pagamento",
                "data_type": "TEXT",
            },
            "payment_date": {
                "description": "Data em que o pagamento foi concluído",
                "data_type": "TEXT",
            },
            "customer_id": {
                "description": "Identificador único do cliente",
                "data_type": "TEXT",
            },
            "customer_name": {
                "description": "Nome completo do cliente",
                "data_type": "TEXT",
            },
            "customer_rating": {
                "description": "Avaliação dada pelo cliente, se aplicável",
                "data_type": "TEXT",
            },
            "sales_channel": {
                "description": "Onde a venda ocorreu: Online, Loja Física",
                "data_type": "TEXT",
            },
            "sales_region": {
                "description": "Região de vendas",
                "data_type": "TEXT",
            },
            "sales_rep": {
                "description": "Representante de vendas",
                "data_type": "TEXT",
            },
            "delivery_status": {
                "description": "Status da entrega",
                "data_type": "TEXT",
            },
            "delivery_date": {
                "description": "Data de entrega",
                "data_type": "TEXT",
            },
            "shipping_cost": {
                "description": "Custo do envio",
                "data_type": "DOUBLE PRECISION",
            },
        },
    }
}
