
from BACK.modules.modules import gmail_inbox , attachment , fb_send_curriculum , get_curriculum


subject_curriculo = [

    
    "currículo",
    "curriculo",
    "cv",
    "c.v.",
    "resume",
    "resumé",
    "curriculum",
    "curriculum vitae",
    "envio de currículo",
    "envio do currículo",
    "enviando currículo",
    "envio de cv",
    "envio do cv",
    "currículo profissional",
    "curriculo profissional",
    "currículo atualizado",
    "curriculo atualizado",

    
    "candidatura",
    "candidatura à vaga",
    "candidatura a vaga",
    "candidatura para vaga",
    "candidatura espontânea",
    "vaga",
    "vaga de emprego",
    "vaga de trabalho",
    "oportunidade",
    "oportunidade de emprego",
    "oportunidade profissional",
    "processo seletivo",
    "processo de seleção",
    "candidato",
    "perfil profissional",
    "apresentação profissional",
    "interesse na vaga",
    "interesse profissional",


    "vendedor externo",
    "supervisor externo",
    "vendedor online",
    "auxiliar administrativo",
    "assistente de rh",
    "analista de ti",
    "jovem aprendiz",
    "operador de caixa",
    "montador",
    "auxiliar mecânico",
    "auxiliar serviços gerais",
    "auxiliar de serviços gerais",
    "assistente de administrativo",
    "assistente administrativo",
    "auxiliar administrativo credere",
    "assistente administrativo emplacamento",
    "assistente administrativo consorcio",
    "assistente administrativo consórcio",
    "vendedora",
    "vendedora show room",
    "vendedora showroom",
    "show room",
    "showroom",
    "assistente de faturamento",
    "jovem aprendiz faturamento",
    "jovem aprendiz pós vendas",
    "jovem aprendiz pós-vendas",
    "estagiário de arquivologia",
    "estagiária contábil",
    "estagiario de arquivologia",
    "estagiaria contabil",
    "estagiária de adm pessoal",
    "estagiario de adm pessoal",
    "estagiário de adm pessoal",
    "garantista",
    "gerente de pós vendas",
    "gerente de pós-vendas",
    "motorista"

]


def process_curriculum():
    
    "puxa o conteudo dos emails"
    inbox      = gmail_inbox(subject_curriculo) 
    "verifica se tem algum anexo e baixa ele em base 64"
    anexo      = attachment(inbox)
    "baixa os curriculos em base 64 e armazena suas informações"
    curriculos = get_curriculum(anexo)
    "manda os curriculos para o fb"
    fb_send_curriculum(curriculos)