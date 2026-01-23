-- =====================================================
-- DIA 3 - CONSULTAS SQL | SUPERSTORE
-- =====================================================

-- 1. Vendas totais por ano (faturamento)

SELECT order_year,
       sum(sales) AS total_sales


FROM superstore
GROUP BY order_year
ORDER BY order_year;

-- -----------------------------------------------------------
-- Vendas por Categoria
SELECT
    category,
    sum(sales) AS sales_per_category
FROM superstore
GROUP BY category
ORDER BY category;
-- --------------------------------------------------------------
-- Vendas por Região
SELECT
    region,
    sum(sales) AS sales_per_region
FROM superstore
GROUP BY region
ORDER BY region;
-- ---------------------------------------------------------------
-- Ticket médio por mês (1 - janeiro ... 12 - dezembro)
SELECT
    order_month,
    avg(sales) AS ticket_medio_mes
FROM superstore 
GROUP BY order_month
ORDER BY order_month;

-- -------------------------------------------------------------
-- 5 estados com mais vendas
SELECT
    state,
    sum(sales) AS vendas_por_estados
FROM superstore
GROUP BY state
ORDER BY state
LIMIT 5;

-- ---------------------------------------------------------------
-- A métrica Percentual de Pedidos não foi calculada tendo em vista que
-- a informação sobre descontontos não aparece no db

-- ------------------------------------------------------------
-- Percentual de pedidos por região
-- Calculado usando window function para evitar subqueries

SELECT 
    region,
    COUNT(*) AS total_orders,
    COUNT(*) * 100 / SUM(COUNT(*)) OVER () AS pct_oders_per_region
FROM superstore
GROUP BY region
ORDER BY region;

-- COUNT(*) representa o número de registros (linhas),
-- não necessariamente pedidos únicos

