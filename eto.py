solange (i < n)  {
    mutex_lock(m);
    mein_i := i;
    i := i + 1;
    mutex_unlock(m);
    if (mein_i < n) {
        a := vektor_a[mein_i];
        b := vektor_b[mein_i];
        s := komplizierte_funktion(a, b);
        ergebnis[mein_i] := s;
    }
}