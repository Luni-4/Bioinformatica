Bioinformatica
================

# Indice

1. [Informazioni](#1-informazioni)
2. [Modalità di lavoro](#2-modalità-di-lavoro)
  1. [Idee](#21-idee)
  2. [Divisione dei compiti](#22-divisione-dei-compiti)
  3. [Link Utili](#23-link-utili)
3. [Input](#3-input)
  1. [Drosophila melanogaster](#31-drosophila-melanogaster)
4. [Output](#4-output)
5. [Dubbi](#5-dubbi)


-----------------

# 1. Informazioni

- Linguaggio di programmazione: Python
- Versione Python: 3.5
- Librerie Python
    - scikit-learn
    - numpy
    - scipy
    - matplotlib
    - python3-tk (sudo apt-get install python3-tk) 

# 2. Modalità di lavoro

## 2.1. Idee

I numeri associati ai punti rappresentano le priorità di risposta alle domande/esecuzione del lavoro. Più i valori sono bassi, più sono importanti.

1.  Adaboost è necessario per Cesa? Oppure possiamo usare solo SVM e Pegasos? Tu cosa ne pensi? In questo modo lui ci chiederebbe solo SVM, i kernel e l’online gradient descent. La scelta di SVM è obbligata se vogliamo fare Pegasos, visto che è un’implementazione particolare di SVM. Potremmo confrontare i risultati ottenuti da entrambi.
2.  Capire come funziona SVM nello spazio dei kernel RBF, cosa succede al variare dei parametri C e gamma? Fare un’analisi approfondita.
3.  Analizzare i risultati ottenuti con il progetto di bioinformatica, capire perché i nostri risultati sono buoni e valutare se il Boxplot è la scelta adeguata
4.  Finire i grafici che volevi aggiungere per Bioinformatica, Pici
5.  Eliminare gli ill-defined, durante l’orale ho notato che il prof non li aveva compresi perché erano troppo legati alla parte implementativa. Spieghiamo il problema di fondo che porta agli ill-defined.
6.  Cercare di risolvere il problema degli ill-defined scegliendo dei pesi più sensati per le classi
7.  Variare le scale dei grafici, perlopiù le ordinate, almeno abbiamo dei risultati più fighi in visualizzazione
8.  Pulire il codice in alcuni punti, se fosse possibile. 
9.  Correggere gli errori grammaticali e le frasi legnose del report
10. Le curve roc e prc le facciamo? Oppure ce ne freghiamo e andiamo avanti? Sarebbe bello perderci un po' di tempo per capire come funzionano. 

## 2.2. Divisione dei compiti

FEDERICO:

- Punti 4 e 8

MICHELE:

- Vorrei occuparmi del punto 2 e del punto 7

## 2.3. Link Utili

- Dati: http://homes.di.unimi.it/valentini/DATA/ProgettoBioinf1617

- Buona spiegazione di AUPRC e AUROC: http://www.chioka.in/differences-between-roc-auc-and-pr-auc/

- Spiegazione sbilanciamento delle classi (Data Imbalance) e possibili metodi per risolverlo: http://www.chioka.in/class-imbalance-problem/

- Metodi di scoring: http://scikit-learn.org/stable/modules/model_evaluation.html#scoring-parameter

- Precision-Recall-Curve: https://classeval.wordpress.com/introduction/introduction-to-the-precision-recall-plot/

- ROC e AUROC: http://www.cs.bris.ac.uk/~flach/ICML04tutorial/ 

- Metriche per classificatori binari, multiclasse, multi-label: http://rali.iro.umontreal.ca/rali/sites/default/files/publis/SokolovaLapalme-JIPM09.pdf


# 3. Input

- OGNI ENTRY DELLA MATRICE É SEPARATA DA UN ALTRA PER MEZZO DI UN TAB
- TENIAMO A 0 I VALORI DELLE DIAGONALI DELLE MATRICI DI ADIACENZA (FINGIAMO CHE NON ESISTANO)


## 3.1. Drosophila melanogaster

- Matrice di adiacenza 3195 x 3195.Un entry della matrice contiene un valore che indica la similarità tra le proteine, individuate dagli indici della entry stessa.

- Matrice delle annotazioni. Un entry della matrice può assumere solo i valori 0 e 1. Il valore 0 significa che la proteina non è associata alla classe, al contrario con 1 la proteina è associata.
    - 3195 x 235 per CC

# 4. Output

- Tanti grafici che mostrino il nostro operato
- Dei buoni confronti tra i classificatori
- Un buon report

# 5. Dubbi

FEDERICO:

MICHI:

Come abbiamo già analizzato nel report.

C è il parametro che controlla la penalizzazione sull'errore di classificazione quando si ha a che fare con training set non linearmente separabili. 
Può essere usato anche senza l'utilizzo di un kernel.

Un C alto comporta un errore di classificazione basso perché penalizza molto la misclassificazione, ma aumenta notevolmente la varianza.


Gamma è uguale a 1/(2 * sigma). Ogni singolo punto viene "sollevato" dalla superficie in maniera tale che, nello spazio iperdimensionale, un iperpiano possa dividere gli esempi. 
Solitamente lo spazio iperdimensionale è a infinite dimensioni. Il "sollevamento" di questi punti è controllato da sigma, quindi da gamma.
Un altro modo per guardare gamma, forse più intuitivo, consiste nel valutare la relazione del singolo esempio xi rispetto agli esempi catalogati come support vectors, ovvero
quegli esempi che violano i vincoli o che hanno margine esattamente uguale a 1. Con un gamma molto basso, la gaussiana sarà molto ampia e l'esempio xi
verrà molto influenzato dai support vectors, mentre con un gamma alto, la gaussiana sarà molto stretta e i support vectors influenzeranno poco.

Gamma alto comporta un errore più alto ma una varianza più bassa, un gamma basso il contrario.

Quello che si vuole fare, è trovare dei valori di gamma e di C che siano bilanciati, in modo da poter controllare la varianza. Da risultati empirici,
si è verificato che i risultati migliori si ottengono quando C è molto elevato e gamma piccolo. Il nostro caso C7_G7 è un esempio.

Sempre da un'analisi empirica, quando gamma assume valore intermedi e C è elevatissimo, i risultati ottenuti non cambiano.

Politica di lavoro:

- Non usare valori di C e di Gamma che crescano o decrescano contemporaneamente, si otterrebbero dei brutti risultati fin da subito.
- Esplorare valori di C e di Gamma inversamente proporzionali tra loro



