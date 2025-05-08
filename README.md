# Sporta Treniņu Plānošanas Lietotne

Šī ir Python lietotne, kas ļauj lietotājiem plānot un sekot līdzi saviem sporta treniņiem, analizēt progresu un saņemt ieteikumus nākamajiem treniņiem, balstoties uz iepriekšējiem rezultātiem. Lietotāji varēs pievienot treniņus, norādīt vingrinājumus, intensitāti, reps, sets un svaru.

## Kādus Libraries mēs izmantojām projektā? 

  - **Tkinter**: 
    - Grafiskās lietotāja saskarnes izveidei. Šī bibliotēka tiek izmantota, lai izveidotu interaktīvas logus, kur lietotājs var pievienot vai rediģēt treniņus, kā arī skatīt statistiku.
  
  - **matplotlib**:
    - Izmantots datu vizualizācijai, piemēram, lai parādītu grafikus par treniņu progresu vai vidējo svaru.
    
  - **MessageBox (Tkinter)**:
    - Lai parādītu informācijas ziņojumus vai kļūdu paziņojumus, piemēram, apstiprinājumu, ka treniņš ir veiksmīgi pievienots vai dzēsts.

## Funkcionalitāte

- **Treniņu pievienošana**: Lietotāji var pievienot treniņus, norādot datumu, vingrinājumus, sets, reps un svaru.
- **Progresu uzskaite**: Lietotāji var sekot līdzi savam progresam, redzot iepriekšējos treniņus.
- **Ieteikumi**: Programma var sniegt ieteikumus nākamajiem treniņiem, balstoties uz lietotāja iepriekšējiem rezultātiem, piemēram, "Mēģiniet palielināt svaru".
- **Datu saglabāšana**: Treniņu dati tiek saglabāti, izmantojot **JSON** formātu, kas nodrošina iespēju saglabāt un ielādēt treniņus nākotnē.

## Instalēšana

### 1. Repozitoriju klonešana
Lai iegūtu projekta failus, izmantojiet Git:

```bash
git clone https://github.com/23DP4MOzol/ProjectX
```

### 2. Bibliotēku instalēšana
Projekts izmanto vairākas Python bibliotēkas, kas jāinstalē pirms lietošanas. Lai to izdarītu, atveriet komandrindu un instalējiet nepieciešamās atkarības, izmantojot `pip`:

```bash
pip install matplotlib
```

## Kā lietot

1. **Palaidiet aplikāciju**:
   - Palaidiet Python skriptu, lai atvērtu lietotni. (main.py)

2. **Pievienojiet treniņu**:
   - Aizpildiet laukus (datums, vingrinājums, sets, reps, svars) un noklikšķiniet uz "Pievienot treniņu".

3. **Skatīt treniņus**:
   - Lietotāji var skatīt savus pievienotos treniņus un to datus.

4. **Rediģēt treniņu**:
   - Lietotāji var rediģēt jau esošos treniņus.

5. **Dzēst treniņu**:
   - Lietotāji var dzēst treniņus pēc izvēles.

6. **Skatīt statistiku**:
   - Lietotāji var apskatīt statistiku par saviem treniņiem, piemēram, kopējo treniņu skaitu un vidējo svaru.

7. **Saņemt ieteikumus**:
   - Pamatojoties uz iepriekšējo treniņu datiem, programma sniedz ieteikumus nākamajiem treniņiem.
