import csv

#criterio para adicionar os posts no linkedin: reacoes dos posts do linkedin muito próximas ou acima de 300
posts_linkedin = []

fields = ["id", 'fonte', 'tipo', "conteudo", 'url']

filename = "posts_linkedin.csv"

def add_post(id, fonte, tipo, conteudo_post, url) :
    return posts_linkedin.append({'id': id, 'fonte': fonte, 'tipo': tipo, 'conteudo': conteudo_post, 'url': url })

add_post(1, 'Linkedin', 'postagem', 'Sua voz nunca será mais importante que seu ouvido. Um líder que se blinda e não ouve seus liderados, deixando a vaidade tomar conta, por mais experiente que seja, está adotando a receita do seu próprio fim. Aqui vão 3 práticas que você precisa aderir para estimular a voz do seu time:--1. Corra atrás. Ninguém vai te dar feedback, seus liderados têm medo. Estimule-os. Pergunte como pode melhorar. Isso te ajuda a encontrar pontos cegos que, sozinho, você não perceberia.--2. Não leve para o ringue. Não interrompa, não queira se justificar.  Escute, por mais que não concorde, e no final faça essas perguntas: - Quais comportamentos você não gosta que eu tenha e acha que devo melhorar? - ‘’O que eu deveria parar e começar a fazer?’’--3. Ambiente seguro. Garanta que seus liderados se sintam confiantes para falar abertamente, sem medo. Mostra que você não só valoriza o feedback deles, como trabalha para melhorar o ponto levantado.Faça com que eles tenham vontade e confiança em poder falar abertamente e que isso não vai gerar um problema futuramente. Jogue o jogo abertamente. Sei que esse tipo de conversa nunca é fácil, eu mesmo demorei para entender que quem dá feedback também precisa estar preparado para receber. Falo sobre isso na minha aula no programa presencial G4 Gestão de Pessoas. Você aprenderá diretamente comigo, Vabo e Bernardinho as práticas de gestão e liderança das empresas que mais crescem no país.', 'https://www.linkedin.com/posts/basaglia_sua-voz-nunca-ser%C3%A1-mais-importante-que-seu-activity-7206282963750207488--hur?utm_source=share&utm_medium=member_desktop')


add_post(2,  'Linkedin', 'postagem',  'Se existe um conselho senso comum que não acredito é “siga o seu sonho”. Sonhos têm como premissa a fantasia e não apego à realidade. E isso não é um problema. O erro está em resumir sua realidade aos sonhos. Sendo mais pragmático: não siga seus sonhos, procure uma atividade em que você é diferenciado. Tão alegre quanto quem realiza o que sonha na carreira é aquela pessoa que se destaca no que se propõe. Seguir nossos sonhos não significa muito, pois nem sempre somos excepcionais em tudo o que queremos. Porém, ao buscar uma atividade onde nos destacamos, encontramos um lugar para crescer e sermos protagonistas de nossas vidas. É onde nossos talentos naturais podem nos levar além do comum. Espero que você seja alguém de sorte, que seu maior talento esteja ligado ao seu sonho de criança. Se como a maioria das pessoas esse não for o caso, faça os dois e brilhe!', 'https://www.linkedin.com/posts/basaglia_se-existe-um-conselho-senso-comum-que-n%C3%A3o-activity-7203802990720229377-cBgW?utm_source=share&utm_medium=member_desktop')


add_post(3,  'Linkedin', 'postagem','Quando alguém se apaixona pelas suas flores e não pelas suas raízes ficará completamente perdido quando o outono ou o inverno chegarem. Isso vale para relacionamentos amorosos, familiares, de amizade ou profissionais.','https://www.linkedin.com/posts/basaglia_quando-algu%C3%A9m-se-apaixona-pelas-suas-flores-activity-7201553154994278402-V83u?utm_source=share&utm_medium=member_desktop')


add_post(4,  'Linkedin', 'postagem', 'Se preocupar com os outros é um dos maiores desperdícios de energia que você poderia ter.Sejamos honestos: os outros não se preocupam tanto assim com você. Mais do que isso, é que certo para um pode não ser para outro, tornando impossível a possibilidade de agradar a todos. Aos poucos, no anseio da popularidade, você se distancia dos seus sonhos. Aos poucos, deixa de ser você. E se ainda não consegui te convencer, nunca se esqueça: a opinião dos outros muda com frequência. Você não só vai desagradar muita gente, você vai desagradar gente que gostava de você e mudou de opinião. Talvez você discorde. Argumente que eu estou ficando velho e acho isso uma excelente colocação. Mas tudo bem, não me importo tanto assim com a opinião dos outros. ', 'https://www.linkedin.com/posts/basaglia_se-preocupar-com-os-outros-%C3%A9-um-dos-maiores-activity-7203365089561710592-IfSq?utm_source=share&utm_medium=member_desktop')


add_post(5,  'Linkedin', 'postagem', 'O segredo do sucesso vai além das habilidades técnicas. É sobre entender profundamente o ambiente ao seu redor. A cultura da empresa, suas regras e, principalmente, as pessoas que compõem esse universo são peças-chave. Investir tempo em compreender esse contexto aumenta sua eficiência e também direciona seus esforços para onde realmente importam. Analise, absorva e adapte-se. É assim que você não apenas sobrevive, mas prospera nesse ambiente desafiador.‌','https://www.linkedin.com/posts/basaglia_o-segredo-do-sucesso-vai-al%C3%A9m-das-habilidades-activity-7197204503312400384-R2qG?utm_source=share&utm_medium=member_desktop')

#542
add_post(6,  'Linkedin', 'postagem', 'Se você quer agradar todo mundo, não seja líder. Venda sorvete. Os maiores lideres são aqueles que sabem dar feedback. Afinal, um executivo que não conversa com seus liderados e não joga o jogo abertamente, por mais experiente que seja, pode estar adotando a receita para o fracasso. Por isso, considere esses pontos na hora da reunião de 1:1 com seu liderado > --1. Jogue limpo Feedback não é elogio, nem todos são agradáveis, mas todos têm valor. Não enrole e jogue o jogo abertamente.-- 2. Esqueça o sanduíche. 70% dos candidatos saem de uma reunião sem saber o que foi elogio e o que foi reclamação. Afinal, a maioria dos líderes dão feedback “sanduíche”, entregam um elogio, depois uma critica e para fechar a reunião com um bom astral fazem mais um feedback positivo. Não funciona.--3. Monte um plano. Depois do feedback o candidato está ansioso para melhorar.Explique o contexto e foque no que deve ser feito dali para frente. Coloque prazos. Mostre o resultado que ele vai ter se alcançar aqueles pontos. Um feedback bem recebido e trabalhado pode destravar novas oportunidades na carreira. Sei que esse tipo de conversa nunca é fácil, tive que aprender muito para me tornar um líder que entrega resultados acima da média. Se você quer aprender sobre contratação, gestão de time, e as práticas de liderança das grandes empresas, participe do G4 Gestão de Pessoas. São 3 dias de conteúdos e mentorias para aprender a liderar times de alta performance.', 'https://www.linkedin.com/posts/basaglia_se-voc%C3%AA-quer-agradar-todo-mundo-n%C3%A3o-seja-activity-7196479707817644032-nC3w?utm_source=share&utm_medium=member_desktop')


with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    
    # Escrever cabeçalhos (field names)
    writer.writeheader()
    
    # Escrever dados (rows)
    for row in posts_linkedin:
        writer.writerow(row)
    

print(f"Arquivo {filename} criado com sucesso!")