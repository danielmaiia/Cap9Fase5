# Cap9Fase5
Cap 9 - Agilidade para Carga de Mercadorias
Você abriu um pequeno negócio de vendas de roupas pela internet. Inicialmente, você mesmo fazia as entregas. Mas o negócio prosperou tanto, que precisou contratar uma empresa de logística para fazer as entregas. Abaixo, há algumas explicações a respeito:

A van da empresa de logística chega no local de expedição das mercadorias às 20h, quando são geradas as ordens com os horários de entrada das mercadorias na fila de carga. A ordem de carga deve ser gerada de maneira aleatória, não ultrapassando o máximo de 15 mercadorias;
Por questão de acomodação no local, a fila de carga pode conter apenas 15 mercadorias por vez;
O motorista da van inicia a carga das mercadorias, sendo a 1ª às 20h10. Ele pode contar com um ajudante, se necessário (2 pessoas na carga);
O tempo de carregar cada mercadoria é X minutos (X=resto da divisão dos últimos 2 dígitos do seu RM por 3 somado a 1; escolha o RM de um dos colegas de seu grupo; anote qual RM foi escolhido);
Para agilizar o processo de carga, são preparadas 3 mercadorias simultaneamente (pode ser menos apenas no momento em que a fila tiver menos do que 3 mercadorias);
A cada 2 minutos, mais uma mercadoria entra na fila;
Quando a 1ª mercadoria é carregada na van, é calculado o tempo de espera usando a informação do papel que o motorista entregou com o horário de entrada.
Para simular uma situação real como essa, é preciso que o programa desenvolvido tenha uma repetição onde cada 10 iterações represente o avanço de 1 minuto no relógio ou utilize uma função que contabilize esse tempo de maneira real.   Conhecendo o tempo requerido para carregar cada mercadoria (X minutos) ou entrar na fila (2 minutos), o programa deve esperar o tempo correto para ocorrerem.

Supondo que a capacidade da van é sempre maior do que a quantidade de mercadorias, o programa deve ser encerrado apenas quando não houver mais nenhuma mercadoria na fila.
