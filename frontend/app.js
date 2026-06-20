const secAcoes = document.getElementById("sec-acoes");
const secNoticias = document.getElementById("sec-noticias");
const tabAcoes = document.getElementById("tab-acoes");
const tabNoticias = document.getElementById("tab-noticias");

tabAcoes.addEventListener("click", () => {
  secAcoes.classList.add("active");
  secNoticias.classList.remove("active");
});

tabNoticias.addEventListener("click", () => {
  secNoticias.classList.add("active");
  secAcoes.classList.remove("active");
});

const tbody = document.querySelector("#table-ativos tbody");
const btnLoadAcoes = document.getElementById("btn-load-acoes");
const btnLoadFiis = document.getElementById("btn-load-fiis");

async function loadAtivos(tipo) {
  tbody.innerHTML = "<tr><td colspan='8'>Carregando...</td></tr>";
  try {
    const url = tipo === "acoes" ? "/api/acoes" : "/api/fiis";
    const res = await fetch(url);
    const data = await res.json();

    tbody.innerHTML = "";
    data.slice(0, 50).forEach(item => {
      const tr = document.createElement("tr");

      const papel = item["Papel"] || item["Código"] || "";
      const cotacao = item["Cotação"] || item["Cotacao"] || "";
      const pl = item["P/L"] || "";
      const pvp = item["P/VP"] || "";
      const roe = item["ROE"] || "";
      const dy = item["Div.Yield"] || "";
      const score = item["score"] || "";

      tr.innerHTML = `
        <td>${papel}</td>
        <td>${tipo.toUpperCase()}</td>
        <td>${cotacao}</td>
        <td>${pl}</td>
        <td>${pvp}</td>
        <td>${roe}</td>
        <td>${dy}</td>
        <td>${score.toFixed ? score.toFixed(2) : score}</td>
      `;
      tbody.appendChild(tr);
    });
  } catch (e) {
    tbody.innerHTML = "<tr><td colspan='8'>Erro ao carregar dados.</td></tr>";
    console.error(e);
  }
}

btnLoadAcoes.addEventListener("click", () => loadAtivos("acoes"));
btnLoadFiis.addEventListener("click", () => loadAtivos("fiis"));

// Notícias – por enquanto, mock; depois podemos integrar com uma API/RSS
const newsList = document.getElementById("news-list");

const mockNews = [
  {
    title: "Automação de processos em mineração com IA",
    summary: "Uso de modelos de machine learning para otimizar rotas de transporte e reduzir custos operacionais.",
    link: "#"
  },
  {
    title: "Segurança de dados em ambientes industriais",
    summary: "Boas práticas de segurança para times de TI em plantas de mineração com redes OT e IT integradas.",
    link: "#"
  },
  {
    title: "Monitoramento em tempo real de produção",
    summary: "Integração de sensores IoT com dashboards para acompanhamento de KPIs de produção.",
    link: "#"
  }
];

mockNews.forEach(n => {
  const card = document.createElement("div");
  card.className = "news-card";
  card.innerHTML = `
    <h3>${n.title}</h3>
    <p>${n.summary}</p>
    <a href="${n.link}" target="_blank">Ler mais</a>
  `;
  newsList.appendChild(card);
});
