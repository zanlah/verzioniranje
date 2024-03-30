import cv2 as cv
import numpy as np

def konvolucija(slika, jedro):
    #todo
    slikaCopy = np.copy(slika)
    #dobim dimenzije slike in jedra
    visina, sirina = slikaCopy.shape
   
    visina_j, sirina_j = jedro.shape

    #ugotovim kako je potrebno razširiti sliko da se ne bo zmanjšala po končanju konvolucije
    razširitev_v = visina_j // 2
    razširitev_š = sirina_j // 2
   
    #razširim robne piksle
    #razširjena_slika = np.pad(slikaCopy, ((razširitev_v, razširitev_v), (razširitev_š, razširitev_š)), 'edge')

    #dodam ničle okoli robov
    razširjena_slika = np.pad(slikaCopy, ((razširitev_v, razširitev_v), (razširitev_š, razširitev_š)), 'constant', constant_values=0)
    rezultat = np.zeros((visina, sirina), dtype=np.float32)
    for i in range(visina):
        for j in range(sirina):
            # Izračunaj uteženo vsoto med jedrom in ustreznim delom razširjene slike
            območje = razširjena_slika[i:i+visina_j, j:j+sirina_j]
            rezultat[i, j] = np.sum(območje * jedro)

    #če je to zakometirano se slika ne prikaže
    #rezultat = cv.normalize(rezultat, None, 0, 255, cv.NORM_MINMAX).astype('uint8')

    return rezultat

def filtriraj_z_gaussovim_jedrom(slika,sigma):
    slikaCopy = np.copy(slika)
    velikost_jedra = int((2*sigma)*2 + 1)

    #srednji index jedra
    k = int(velikost_jedra / 2  - 0.5 )

    jedro = np.zeros((velikost_jedra, velikost_jedra), dtype=np.float32)

    for i in range(velikost_jedra):
        for j in range(velikost_jedra):
            x = i - k
            y = j - k
            jedro[i, j] = (1 / (2 * np.pi * sigma**2)) * np.exp(-(x**2 + y**2) / (2 * sigma**2))

    # Normalizacija jedra - vsota vseh elementov je enaka 1, če je to zakomentirani se slika ne prikaže       
    #jedro /= jedro.sum()
    return konvolucija(slikaCopy, jedro)

def filtriraj_sobel_smer(slika):
    '''Filtrira sliko z Sobelovim jedrom in označi gradiente v orignalni sliki glede na ustrezen pogoj.'''
    pass

if __name__ == '__main__':
    slika1 = np.array([[1, 0, 0, 0],
                    [0, 2, 0, 0],
                    [0, 0, 3, 0],
                    [0, 0, 0, 4]], dtype=np.float32)
    
    ###########
    # 1 0 0 0 #
    # 0 2 0 0 #
    # 0 0 3 0 #
    # 0 0 0 4 #
    ###########
    jedro = np.array([[1, 1, 1],
                     [1, 1, 1],
                     [1, 1, 1]])
    
    slika_konvolucija = konvolucija(slika1, jedro)
    slika_gauss = filtriraj_z_gaussovim_jedrom(slika1, 1.4)

    # Prikažemo izvirno sliko
    print("Original:\n {}".format(slika1))
    print("Konvolucija:\n {}".format(slika_konvolucija))
    print("Gauss:\n {}".format(slika_gauss))     
    pass