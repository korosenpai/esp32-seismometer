# il sismografo


# indice



* perché monitorare il terreno
* primo sismografo -> zhang heng
* sismografi oggi
* sismografo diy
* sismografo a 1 componente
* problema
* sismografo a 3 componenti
* come funziona la scala Richter e Mercalli 
* trovare il magnitudo di un terremoto simulato
* come trovare epicentro di terremoto con triangolazione
* predirre terremoti con radon e thoron


# perché monitorare il terreno?

I terremoti sono vibrazioni causate dalla rottura di rocce sotterranee per lo stress.

possono essere molto catastrofici, quindi vengono studiati per trovare modi per prepararsi e limitare i danni da essi.


# zhang heng

nato: 78

morto: 139

è stato un geofisico, poeta cinese e inventore

ai tempi non si sapeva delle placche tettoniche e si pensava che i terremoti fossero dovuti a sbilanci nello yin e yang

è stato l’inventore del sismografo.

È costituito da 8 sfere di bronzo e un pendolo.

quando un terremoto avveniva la sfera più vicino all'epicentro del terremoto sarebbe caduta dal vaso.

Riuscì a rilevare un terremoto a 450 km di distanza che non fu sentito dai civili vicino al sismografo


## funzionamento

l’oggetto è andato perduto quindi non sappiamo bene come funziona, ma abbiamo delle teorie:

<img src = "https://preview.redd.it/ny3ualbq5gp71.jpg?auto=webp&s=c476fe70e56c5899db4e52523f663b71368bf698" alt="zhang heng’s seismograph" title="ipotesi di funzionamento" width="50%" height="auto" />


# SISMOGRAFO

I sismografi registrano i movimenti della terra.

alcuni sono messi sotto terra, così riescono a sentire meglio l’arrivo di un'onda di sismica/vibrazione.

sismografi moderni:

composti da pendolo che oscilla sopra un rullo con un foglio che sta ruotando.

il pendolo comincia a oscillare quando ci sono delle vibrazioni.

si attacca penna a pendolo -> scrive oscillazione su foglio

no vibrazioni -> linea dritta e calma

si vibrazioni -> pennetta si muove oscillando


# DIY

microcontroller

custom pcb -> circuito

sensore imu


## esp32

microcomputer a bassa potenza solitamente utilizzato per la progettazione di strumenti IOT.


## mpu9250

IMU - inertial measurement unit, misura l accelerazione e l’accelerazione angolare subita.

include anche un magnetometro, per misurare il campo magnetico,  e un termometro

( utilizzeremo solo accelerometro)


## tecnologia MEMS

sensori imu funzionano con tecnologia MEMS

Il sensore ha struttura a pettine.

ogni “pettine” e la parete forma un condensatore -> la distanza tra le microstrutture determina la loro capacità

parte blu -> oscilla in base ad accelerazione -> cambio di capacità rilevato dal sensore che lo converte in valore di accelerazione


## funzionamento

diagramma di flusso mostrato nella presentazione


## rilevamenti / grafico

mostrare sismografo

sommando le accelerazioni rilevate otteniamo un grafico del genere


## problema

quale è?

riuscite a distinguere da dove arrivano le scosse? con quanta intensità?

questo metodo si limita a sommare forze.

sorgono diversi problemi:



* quando scuoto per le assi x positive ma y negative -> forze si sottraggono
* terremoto arriva da in basso a sinistra mentre altro da x negativa, non si capisce direzione. Se x è positivo ma y è negativo le onde si annullano, non si capisce forza
* poca chiarezza

il grafico rimane comunque buono per avere una comprensione basica delle scosse


## sismografi a 3 componenti


### passaggio da 1 component a 3 component

ci sono certi edge cases che mostrano dati falsi, con un solo grafico non possiamo accuratamente rappresentare onde rilevate

risulta quindi utile separare ogni onda rivelata nel suo grafico appropriato

MOSTRARE 3-component.py

notare come su asse z il livello di base è 9.qualcosa, questo per …? accelerazione di gravità


## analisi tipo di onde

3 onde diverse -> p, s, surface

stazione di sismogramma producono 3 sismogrammi per ogni terremoto

movimento sulla terra è tridimensionale -> x, y, z -> un componente riflette solo una direzione

durante un terremoto la casa si può muovere in tutte le direzioni

onde p, s viaggiano sotto terra -> traiettoria curva per la curvatura della terra

(vedere immagini)

onde p affettano più verticale e arrivano prima

onde s sono piu lente e distruttive, muove più in direzioni x, y e meno su z

onde surface -> si muovo in onda ondulante piu complessa -> appaiono in tutti i componenti

combinazione di questi dati da distanza magnitudo e tipo di terremoto


# scala richter

sviluppata nel 1935 da Charles Richter e Beno Gutenberg del California Institute of Technology per esprimere la magnitudo di un terremoto, ovvero una stima dell'energia sprigionata all'epicentro della frattura della crosta terrestre.


## come funziona?

è logaritmico, quindi aumentare di un punto sarebbe come per moltiplicare per 10:



* 3 -> 4  => 10 volte più potente
* 3 -> 7 => 10000 volte più potente

i terremoti sono tutti diversi, le roccie scivolano, si scontrano e possono causare un terremoto, ma bisogna ricordare che anche l'attrito, la pressione, la profondità, il tipo di roccia sono fattori importanti, convertirlo in un solo numero di scla sembra un'impresa impossibile

controlla solo la quantità di energia rilasciata da un terremoto ma non di cosa siano state le conseguenze

esempio:



* terremoto di magn. 7.8 in nepal 2015 aprile 25
    * distrusse edifici, uccise migliaia e causò una valanga
* terremoto di magn. 7.3 in nepal 2015 maggio 12
    * causò panico e uccise una decina di persone

fa veramente cosi tanta differenza 0.5? dipende dal contesto e tutte le variabili elencate prima.

La magnitudo viene calcolata come il logaritmo in base dieci del massimo spostamento della traccia rispetto allo zero, espresso in micrometri, su un sismografo a torsione di Wood-Anderson calibrato in maniera standard, se l'evento si fosse verificato a una distanza epicentrale di 100 km


## problemi

La scala Richter presenta alcune limitazioni importanti.



* i valori della scala Richter sono solo debolmente correlati con le caratteristiche fisiche della causa dei terremoti. In altre parole, la scala Richter non è in grado di fornire informazioni precise sulla natura del sisma e sulla sua causa, ma si limita a misurare l'energia sprigionata dal terremoto.
* si presenta un effetto di saturazione verso le magnitudini 8,3-8,5, a causa del quale i tradizionali metodi di magnitudine danno lo stesso valore per eventi chiaramente differenti. Questo significa che la scala Richter risulta inefficace per magnitudo superiori a 9 gradi, perché emettono frequenze più basse rispetto a 0,8 Hz. questo problema viene risolto dalla scala di magnitudo del momento sismico.


## scala di magnitudo del momento sismico

rimpiazza scala richter nel 1979

usa gli stessi nomi

usa computer per creare dei sismogrammi sintetici per determinare come il terremoto ha rilasciato energia (triangolazione) => quanto un pezzo di terra si è mosso e quanto forza è stata necessaria

molto più preciso, funziona sopra magnitudo 8, cosa che richter non può


## la scala di mercalli

misura intensità, serve per capire come il terremoto è stato percepito sulla superficie.

sviluppata nel 1930 e usa numeri romani (da I a XII)

sistema molto soggettivo.


# calcola il magnitudo

guardando sismogramma:

```

onda base: senza scosse

primo salto: arrivo onda p

secondo salto: arrivo onda s

```

altezza più grande raggiunta da onda s sopra l'onda base (positiva) => `ampiezza`

tempo di lag: arrivo di onda p a arrivo onda s => `distanza`

```

PER SCALA IMPOSTA:

moltiplico ampiezza per 5

moltiplico distanza per 10

```

usiamo questi valori sul grafico per vedere magnitudo di richter

<img src = "https://www.distar.unina.it/images/ricerca/schema_di_calcolo_della_magnitudo.gif" alt="grafico per calcolare magnitudo" title="come calcolare il magnitudo in scala ritcher" width="50%" height="auto" />


# troviamo l’epicentro

scopriamo ora invece come trovare l’epicentro di un terremoto utilizzando la triangolazione.

ci serve un minimo di 3 stazioni sismiche

determiniamo la `distanza dall’epicentro` di ognuna

<img src = "https://www.vialattea.net/spaw/image/geologia/DistanzaEpicentro/06-dromocrome.jpg" alt="grafico per calcolare distanza da epicentro" title="come calcolare distanza da epicentro" width="50%" height="auto" />

es: 

stazione 1: 700km

non sappiamo l epicentro in quale direzione sia, quindi disegniamo un cerchio con raggio di 700 km => l’epicentro si trova da qualche parte in quel cerchio

stazione 2: 3000km

disegnamo cerchio => ci darà 2 intersezioni con cerchio di stazione 1 => 2 possibili luoghi per epicentro

stazione 3: 3500km

disegnamo cerchio => interseca stazione 1, 2 in un punto singolo => abbiamo trovato posizione di epicentro

questo viene chiamato il metodo della `triangolazione`


# radon and thoron

Prima del terremoto in Giappone del 2011, ricercatori hanno rilevato grandi quantità della coppa di isotopi radon e thoron nei loro territori.

prima del terremoto la pressione aumenta su superfici => microfratture nel terreno fanno uscire gas

Costruire reti di rilevamento di questi isotopi potrebbe essere un nuovo metodo innovativo per avvisare quando un terremoto sta per accadere => potenzialmente fino a 7 giorni di anticipo


# webgrafia

[https://www.youtube.com/watch?v=GcNVpMZlIDo](https://www.youtube.com/watch?v=GcNVpMZlIDo)

[https://www.youtube.com/watch?v=pmf4TXroRJM](https://www.youtube.com/watch?v=pmf4TXroRJM)

[https://it.wikipedia.org/wiki/Unit%C3%A0_di_misura_inerziale](https://it.wikipedia.org/wiki/Unit%C3%A0_di_misura_inerziale)

[https://www.youtube.com/watch?v=Za_22xo7ZQQ](https://www.youtube.com/watch?v=Za_22xo7ZQQ)

[https://www.youtube.com/watch?v=nl9jiubdlXU](https://www.youtube.com/watch?v=nl9jiubdlXU)

[https://www.youtube.com/watch?v=NaNw9LHq9dc](https://www.youtube.com/watch?v=NaNw9LHq9dc)

[https://www.youtube.com/watch?v=zFKI1iPmetY](https://www.youtube.com/watch?v=zFKI1iPmetY)

[https://www.phind.com/search?cache=a0dc474d-03f3-416f-a0ec-f8ce1d5b8d10](https://www.phind.com/search?cache=a0dc474d-03f3-416f-a0ec-f8ce1d5b8d10)

[https://www.youtube.com/watch?v=oBS7BKqHRhs](https://www.youtube.com/watch?v=oBS7BKqHRhs)
