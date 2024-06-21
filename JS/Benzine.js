function kanBereikenTankstation(kilometersNaarTankstation, kilometersPerLiter, resterendeLiters) {
    bereik = false

    aantal_lieters_nodig = resterendeLiters * kilometersPerLiter
    afstand_rijden = aantal_lieters_nodig - kilometersNaarTankstation

    if (afstand_rijden < 0){
        bereik = false
        return bereik

    } else if(kilometersNaarTankstation >= 0){
        bereik = true
        return bereik
    }

    return bereik;
    
}
