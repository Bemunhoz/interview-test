-- Quais as 10 operadoras com maiores despesas em "EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR" no último trimestre?
SELECT 
    reg_ans, 
    descricao, 
    SUM(vl_saldo_final) AS total_despesas
FROM operadoras
WHERE descricao LIKE '%EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE%'
  AND data BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY reg_ans, descricao
ORDER BY total_despesas DESC
LIMIT 10;

-- Quais as 10 operadoras com maiores despesas nessa categoria no último ano?
SELECT 
    reg_ans, 
    descricao, 
    SUM(vl_saldo_final) AS total_despesas
FROM operadoras
WHERE descricao LIKE '%EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE%'
  AND YEAR(data) = 2024
GROUP BY reg_ans, descricao
ORDER BY total_despesas DESC
LIMIT 10;