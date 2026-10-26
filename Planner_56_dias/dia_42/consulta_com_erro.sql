SELECT c.regiao, AVG(p.valor) AS gasto_por_cliente FROM clientes c JOIN pedidos p ON c.cliente=p.cliente GROUP BY c.regiao;
