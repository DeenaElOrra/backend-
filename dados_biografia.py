import csv

biografias = []

fields = ["id", 'fonte', 'tipo', "conteudo", 'url']
filename = "biografias.csv"

def add_biografias(id, fonte, tipo, conteudo_post, url):
    return biografias.append({'id': id, 'fonte': fonte, 'tipo': tipo, 'conteudo': conteudo_post, 'url': url })


add_biografias(1, 'One page', 'biografia', 'Ricardo Basaglia é Mestre em Administração de Empresas pela FGV/EAESP com extensão em Behavioral Science of Management pela Universidade de Yale. Iniciou a carreira na área de tecnologia, atuou em projetos de transformação digital em grandes corporações, mas descobriu que sua grande paixão estava em transformar a vida das pessoas. Ingressou na Michael Page em 2007, responsável pelo startup de negócios e escritórios no país. Hoje como CEO do PageGroup , lidera as operações da Michael Page, Page Personnel, Page Executive, Page Outsourcing e Page Interim no Brasil. É autor do best-seller Lugar de Potência: Lições de carreira e liderança de mais de 10 mil entrevistas, cafés e reuniões. Produzindo conteúdo de carreira e liderança em redes sociais (@ricbasaglia) e no podcast Lugar de Potência, se consolidou como o headhunter mais acompanhado do Brasil, impactando milhares de pessoas diariamente.', 'https://docs.google.com/document/d/1hQFFmuFnQ8XxO9QmzKfQ_0_CZQOyhm7IlJKnA79iNX8/edit?usp=sharing')

add_biografias(2, 'Linkedin', 'biografia', 'Já são mais de 10 mil entrevistas, cafés e reuniões com executivos e empresas de todo Brasil, uma rotina que faz parte da minha vida há quase 20 anos, desde que estou na Michael Page, a maior empresa de recrutamento da América Latina. Hoje, sou CEO da empresa no Brasil. Isso me trouxe aprendizados importantes. Um deles é que a capacidade de nos adaptarmos é um dos principais ativos de qualquer profissional hoje em dia, diante de um mundo altamente dinâmico e imprevisível. Conhecimento só é transformador se for compartilhado, por isso, procuro mostrar quais são os comportamentos, habilidades, hábitos e crenças de grandes líderes do Brasil e do mundo, indivíduos que ‘chegaram lá’ para ajudar mais pessoas a extraírem seu potencial e também chegarem no seu Lugar de Potência. Faço isso para mais de 3 milhões de pessoas que me dão o privilégio de acompanhar os meus conteúdos todos os meses, nas minhas redes sociais, na coluna do Estadão e na Exame, na Rádio Eldorado e no meu podcast Lugar de Potência. Também divido esses insights no livro "Lugar de Potência: Lições de carreira e liderança de mais de 10 mil entrevistas, cafés e reuniões“. Sou Mentor em Gestão de Pessoas no G4 Educação e palestrante.Para chegar aqui, me preparei muito. Além de estar sempre conectado ao meu learning circle, estudei em instituições internacionais como a Harvard, Yale e Fudan Shanghai.', 'https://www.linkedin.com/in/basaglia/')

add_biografias(3, 'G4', 'biografia','CEO da Michael Page Brasil, a maior empresa de recrutamento da América Latina, Basaglia possui vasta expertise em liderança, gestão de pessoas, relações interpessoais e gestão de carreira, tendo mais de 10.000 entrevistas que comprovam o seu track record. Além disso, consolidou-se como headhunter mais acompanhado do Brasil nas redes sociais com a sua ampla experiência em formar equipes fortes nos mais diversos tipos de companhias. É, ainda, autor do best-seller intitulado "Lugar de Potência: Lições de carreira e liderança de mais de 10 mil entrevistas, cafés e reuniões" Hoje, ele também é mentor em Gestão de Pessoas no G4 Educação. Trajetória: --Ricardo Basaglia se formou em processamento de dados na ETEC e no Centro Universitário Rio Preto. Ele também fez uma especialização na PUC-Campinas e estudou administração em instituições internacionais como a Harvard Business School e a Yale School of Management, além de um mestrado na FGV.  Aos 20 anos, criou um portal de internet, ainda quando essa tecnologia estava incipiente no Brasil, e foi procurado por um grupo de investidores que desejavam comprar o projeto. Após essa experiência de ingressar no mercado corporativo, começou sua trajetória profissional na área de tecnologia no Sistema SETA de Ensino, tendo participado de iniciativas e projetos de transformação digital em grandes companhias. No entanto, descobriu que a sua verdadeira vocação era atuar para impactar positivamente a vida das pessoas. Em 2001, atuou como gerente de projetos de internet da Vivo e em 2003 migrou para o setor comercial da Spread. Finalmente, em 2007, recebeu o convite para atuar como diretor executivo da Page Personnel (parte do Group Page no Brasil), onde foi traçando novos caminhos e descobrindo novas possibilidades, tendo sido responsável por estabelecer novos negócios e escritórios no país. Atualmente, como CEO do PageGroup, lidera as operações da Michael Page, Page Personnel, Page Executive, Page Outsourcing e Page Interim no Brasil.--Michael Page: Fundada em 1976 e presente no Brasil desde 2000, a organização possui atuação em mais de 30 países nos 5 continentes. De consultor de treinamento a diretor-executivo, Basaglia ocupou diversos cargos de liderança na empresa. O seu itinerário profissional é repleto de desafios e muito aprendizado na empresa-líder de recrutamento e seleção de profissionais para posições de alta e média gerência em todo o mundo. Como CEO, Basaglia é responsável por liderar as operações da Michael Page Brasil, incluindo a definição de estratégias, a gestão de equipes e a garantia da qualidade dos serviços prestados aos clientes, garantindo que a empresa continue a crescer e se destacar no mercado.', 'https://g4educacao.com/biografias/ricardo-basaglia')

add_biografias(4, 'PUCRS Online', 'biografia','Ricardo Basaglia é Mestre em Administração de Empresas pela FGV/EAESP com extensão pela Universidade de Yale em Behavioral Science of Management. Iniciou a carreira na área de tecnologia, atuou em projetos de transformação digital em grandes corporações, mas descobriu que sua grande paixão estava em transformar a vida das pessoas. Ingressou na Michael Page em 2007, responsável pelo startup de negócios e escritórios no país. Hoje como Diretor Geral, lidera as operações da Michael Page e Page Personnel no Brasil.', 'https://online.pucrs.br/professores/ricardo-basaglia')

with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    
    # Escrever cabeçalhos (field names)
    writer.writeheader()
    
    # Escrever dados (rows)
    for row in biografias:
        writer.writerow(row)
    

print(f"Arquivo {filename} criado com sucesso!")