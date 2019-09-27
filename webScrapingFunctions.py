import requests as rq
from bs4 import BeautifulSoup as bs
def table_scrape(website, debug):
    if debug == False:
        #makes an  html request to the given site
        r = rq.get(website, verify=False)
        html_doc = r.content
    else: 
        #sample html file used to limit html requests to imdb when debugging
        html_doc = """
        <table class="cast_list">
  <tbody><tr><td colspan="4" class="castlist_label"></td></tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0000375/?ref_=ttfc_fc_cl_i1"><img height="44" width="32" alt="Robert Downey Jr." title="Robert Downey Jr." src="https://m.media-amazon.com/images/M/MV5BNzg1MTUyNDYxOF5BMl5BanBnXkFtZTgwNTQ4MTE2MjE@._V1_UX32_CR0,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm0000375/?ref_=ttfc_fc_cl_t1"> Robert Downey Jr.
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0000375?ref_=ttfc_fc_cl_t1">Tony Stark</a> /  
            <a href="/title/tt4154756/characters/nm0000375?ref_=ttfc_fc_cl_t1">Iron Man</a> 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm1165110/?ref_=ttfc_fc_cl_i2"><img height="44" width="32" alt="Chris Hemsworth" title="Chris Hemsworth" src="https://m.media-amazon.com/images/M/MV5BOTU2MTI0NTIyNV5BMl5BanBnXkFtZTcwMTA4Nzc3OA@@._V1_UX32_CR0,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm1165110/?ref_=ttfc_fc_cl_t2"> Chris Hemsworth
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm1165110?ref_=ttfc_fc_cl_t2">Thor</a> 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0749263/?ref_=ttfc_fc_cl_i3"><img height="44" width="32" alt="Mark Ruffalo" title="Mark Ruffalo" src="https://m.media-amazon.com/images/M/MV5BNDQyNzMzZTMtYjlkNS00YzFhLWFhMTctY2M4YmQ1NmRhODBkXkEyXkFqcGdeQXVyNjcyNzgyOTE@._V1_UY44_CR1,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm0749263/?ref_=ttfc_fc_cl_t3"> Mark Ruffalo
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0749263?ref_=ttfc_fc_cl_t3">Bruce Banner</a> /  
            <a href="/title/tt4154756/characters/nm0749263?ref_=ttfc_fc_cl_t3">Hulk</a> 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0262635/?ref_=ttfc_fc_cl_i4"><img height="44" width="32" alt="Chris Evans" title="Chris Evans" src="https://m.media-amazon.com/images/M/MV5BMTU2NTg1OTQzMF5BMl5BanBnXkFtZTcwNjIyMjkyMg@@._V1_UX32_CR0,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm0262635/?ref_=ttfc_fc_cl_t4"> Chris Evans
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0262635?ref_=ttfc_fc_cl_t4">Steve Rogers</a> /  
            <a href="/title/tt4154756/characters/nm0262635?ref_=ttfc_fc_cl_t4">Captain America</a> 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0424060/?ref_=ttfc_fc_cl_i5"><img height="44" width="32" alt="Scarlett Johansson" title="Scarlett Johansson" src="https://m.media-amazon.com/images/M/MV5BMTM3OTUwMDYwNl5BMl5BanBnXkFtZTcwNTUyNzc3Nw@@._V1_UY44_CR2,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm0424060/?ref_=ttfc_fc_cl_t5"> Scarlett Johansson
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0424060?ref_=ttfc_fc_cl_t5">Natasha Romanoff</a> /  
            <a href="/title/tt4154756/characters/nm0424060?ref_=ttfc_fc_cl_t5">Black Widow</a> 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0000332/?ref_=ttfc_fc_cl_i6"><img height="44" width="32" alt="Don Cheadle" title="Don Cheadle" src="https://m.media-amazon.com/images/M/MV5BNDMxNDM3MzY5N15BMl5BanBnXkFtZTcwMjkzOTY4MQ@@._V1_UY44_CR1,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm0000332/?ref_=ttfc_fc_cl_t6"> Don Cheadle
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0000332?ref_=ttfc_fc_cl_t6">James Rhodes</a> /  
            <a href="/title/tt4154756/characters/nm0000332?ref_=ttfc_fc_cl_t6">War Machine</a> 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm1212722/?ref_=ttfc_fc_cl_i7"><img height="44" width="32" alt="Benedict Cumberbatch" title="Benedict Cumberbatch" src="https://m.media-amazon.com/images/M/MV5BMjE0MDkzMDQwOF5BMl5BanBnXkFtZTgwOTE1Mjg1MzE@._V1_UX32_CR0,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm1212722/?ref_=ttfc_fc_cl_t7"> Benedict Cumberbatch
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm1212722?ref_=ttfc_fc_cl_t7">Doctor Strange</a> 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm4043618/?ref_=ttfc_fc_cl_i8"><img height="44" width="32" alt="Tom Holland" title="Tom Holland" src="https://m.media-amazon.com/images/M/MV5BNTAzMzA3NjQwOF5BMl5BanBnXkFtZTgwMDUzODQ5MTI@._V1_UY44_CR2,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm4043618/?ref_=ttfc_fc_cl_t8"> Tom Holland
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm4043618?ref_=ttfc_fc_cl_t8">Peter Parker</a> /  
            <a href="/title/tt4154756/characters/nm4043618?ref_=ttfc_fc_cl_t8">Spider-Man</a> 
                  
          </td>
      </tr>https://www.imdb.com/title/tt0073195/?ref_=fn_al_tt_1
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm1569276/?ref_=ttfc_fc_cl_i9"><img height="44" width="32" alt="Chadwick Boseman" title="Chadwick Boseman" src="https://m.media-amazon.com/images/M/MV5BMTk2OTY5MzcwMV5BMl5BanBnXkFtZTgwODM4MDI5MjI@._V1_UX32_CR0,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm1569276/?ref_=ttfc_fc_cl_t9"> Chadwick Boseman
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm1569276?ref_=ttfc_fc_cl_t9">T'Challa</a> /  
            <a href="/title/tt4154756/characters/nm1569276?ref_=ttfc_fc_cl_t9">Black Panther</a> 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0757855/?ref_=ttfc_fc_cl_i10"><img height="44" width="32" alt="Zoe Saldana" title="Zoe Saldana" src="https://m.media-amazon.com/images/M/MV5BMTM2MjIwOTc0Nl5BMl5BanBnXkFtZTcwNzQ5ODM1Mw@@._V1_UX32_CR0,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm0757855/?ref_=ttfc_fc_cl_t10"> Zoe Saldana
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0757855?ref_=ttfc_fc_cl_t10">Gamora</a> 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm2394794/?ref_=ttfc_fc_cl_i11"><img height="44" width="32" alt="Karen Gillan" title="Karen Gillan" src="https://m.media-amazon.com/images/M/MV5BMTQwMDQ0NDk1OV5BMl5BanBnXkFtZTcwNDcxOTExNg@@._V1_UX32_CR0,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm2394794/?ref_=ttfc_fc_cl_t11"> Karen Gillan
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm2394794?ref_=ttfc_fc_cl_t11">Nebula</a> 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm1089991/?ref_=ttfc_fc_cl_i12"><img height="44" width="32" alt="Tom Hiddleston" title="Tom Hiddleston" src="https://m.media-amazon.com/images/M/MV5BNWYwODAyZjAtOTQ1My00MDY2LTg0NDQtZGFiMDRiYzY4ZmM2XkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_UY44_CR0,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm1089991/?ref_=ttfc_fc_cl_t12"> Tom Hiddleston
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm1089991?ref_=ttfc_fc_cl_t12">Loki</a> 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0079273/?ref_=ttfc_fc_cl_i13"><img height="44" width="32" alt="Paul Bettany" title="Paul Bettany" src="https://m.media-amazon.com/images/M/MV5BNjUzMDIzNjkxMl5BMl5BanBnXkFtZTgwNjgyNzA0MjI@._V1_UY44_CR17,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm0079273/?ref_=ttfc_fc_cl_t13"> Paul Bettany
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0079273?ref_=ttfc_fc_cl_t13">Vision</a> 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0647634/?ref_=ttfc_fc_cl_i14"><img height="44" width="32" alt="Elizabeth Olsen" title="Elizabeth Olsen" src="https://m.media-amazon.com/images/M/MV5BMjEzMjA0ODk1OF5BMl5BanBnXkFtZTcwMTA4ODM3OQ@@._V1_UX32_CR0,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm0647634/?ref_=ttfc_fc_cl_t14"> Elizabeth Olsen
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0647634?ref_=ttfc_fc_cl_t14">Wanda Maximoff</a> /  
            <a href="/title/tt4154756/characters/nm0647634?ref_=ttfc_fc_cl_t14">Scarlet Witch</a> 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm1107001/?ref_=ttfc_fc_cl_i15"><img height="44" width="32" alt="Anthony Mackie" title="Anthony Mackie" src="https://m.media-amazon.com/images/M/MV5BMTk3NTM1MjE2M15BMl5BanBnXkFtZTcwNzc5OTI2Mg@@._V1_UY44_CR1,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm1107001/?ref_=ttfc_fc_cl_t15"> Anthony Mackie
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm1107001?ref_=ttfc_fc_cl_t15">Sam Wilson</a> /  
            <a href="/title/tt4154756/characters/nm1107001?ref_=ttfc_fc_cl_t15">Falcon</a> 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm1659221/?ref_=ttfc_fc_cl_i16"><img height="44" width="32" alt="Sebastian Stan" title="Sebastian Stan" src="https://m.media-amazon.com/images/M/MV5BNTk2OGU4NzktODhhOC00Nzc2LWIyNzYtOWViMjljZGFiNTMxXkEyXkFqcGdeQXVyMTE1NTQwOTk@._V1_UY44_CR1,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm1659221/?ref_=ttfc_fc_cl_t16"> Sebastian Stan
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm1659221?ref_=ttfc_fc_cl_t16">Bucky Barnes</a> /  
            <a href="/title/tt4154756/characters/nm1659221?ref_=ttfc_fc_cl_t16">Winter Soldier</a> 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0252961/?ref_=ttfc_fc_cl_i17"><img height="44" width="32" alt="Idris Elba" title="Idris Elba" src="https://m.media-amazon.com/images/M/MV5BNzEzMTI2NjEyNF5BMl5BanBnXkFtZTcwNTA0OTE4OA@@._V1_UX32_CR0,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm0252961/?ref_=ttfc_fc_cl_t17"> Idris Elba
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0252961?ref_=ttfc_fc_cl_t17">Heimdall</a> 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm1775091/?ref_=ttfc_fc_cl_i18"><img height="44" width="32" alt="Danai Gurira" title="Danai Gurira" src="https://m.media-amazon.com/images/M/MV5BNjYyNjg1OTU1M15BMl5BanBnXkFtZTgwNzYyNTkzMDI@._V1_UX32_CR0,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm1775091/?ref_=ttfc_fc_cl_t18"> Danai Gurira
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm1775091?ref_=ttfc_fc_cl_t18">Okoye</a> 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0227759/?ref_=ttfc_fc_cl_i19"><img height="44" width="32" alt="Peter Dinklage" title="Peter Dinklage" src="https://m.media-amazon.com/images/M/MV5BMTM1MTI5Mzc0MF5BMl5BanBnXkFtZTYwNzgzOTQz._V1_UY44_CR1,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm0227759/?ref_=ttfc_fc_cl_t19"> Peter Dinklage
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0227759?ref_=ttfc_fc_cl_t19">Eitri</a> 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0938950/?ref_=ttfc_fc_cl_i20"><img height="44" width="32" alt="Benedict Wong" title="Benedict Wong" src="https://m.media-amazon.com/images/M/MV5BNTNlMjg3NWQtZmJlNS00NGU2LWI5NWMtZDk2MGI1YTI4YTVkXkEyXkFqcGdeQXVyMTgyMzY5MTk@._V1_UX32_CR0,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm0938950/?ref_=ttfc_fc_cl_t20"> Benedict Wong
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0938950?ref_=ttfc_fc_cl_t20">Wong</a> 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm2962353/?ref_=ttfc_fc_cl_i21"><img height="44" width="32" alt="Pom Klementieff" title="Pom Klementieff" src="https://m.media-amazon.com/images/M/MV5BMTkzNjE5MzY5M15BMl5BanBnXkFtZTgwMDI5ODMxODE@._V1_UY44_CR15,0,32,44_AL_.jpg" class="loadlate"></a>          </td>
          <td>
<a href="/name/nm2962353/?ref_=ttfc_fc_cl_t21"> Pom Klementieff
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm2962353?ref_=ttfc_fc_cl_t21">Mantis</a> 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm1176985/?ref_=ttfc_fc_cl_i22"><img height="44" width="32" alt="Dave Bautista" title="Dave Bautista" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BNTZkYzU0ZGUtZTk1MC00MzJjLWFmMzItY2M0ODY1ZmI2OGQ0XkEyXkFqcGdeQXVyMjI0MjgwNjc@._V1_UY44_CR23,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm1176985/?ref_=ttfc_fc_cl_t22"> Dave Bautista
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm1176985?ref_=ttfc_fc_cl_t22">Drax</a> 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0004874/?ref_=ttfc_fc_cl_i23"><img height="44" width="32" alt="Vin Diesel" title="Vin Diesel" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMjExNzA4MDYxN15BMl5BanBnXkFtZTcwOTI1MDAxOQ@@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm0004874/?ref_=ttfc_fc_cl_t23"> Vin Diesel
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0004874?ref_=ttfc_fc_cl_t23">Groot</a> 
  
  
  (voice)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0177896/?ref_=ttfc_fc_cl_i24"><img height="44" width="32" alt="Bradley Cooper" title="Bradley Cooper" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMjM0OTIyMzY1M15BMl5BanBnXkFtZTgwMTg0OTE0NzE@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm0177896/?ref_=ttfc_fc_cl_t24"> Bradley Cooper
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0177896?ref_=ttfc_fc_cl_t24">Rocket</a> 
  
  
  (voice)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0000569/?ref_=ttfc_fc_cl_i25"><img height="44" width="32" alt="Gwyneth Paltrow" title="Gwyneth Paltrow" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BNzIxOTQ1NTU1OV5BMl5BanBnXkFtZTcwMTQ4MDY0Nw@@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm0000569/?ref_=ttfc_fc_cl_t25"> Gwyneth Paltrow
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0000569?ref_=ttfc_fc_cl_t25">Pepper Potts</a> 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0001125/?ref_=ttfc_fc_cl_i26"><img height="44" width="32" alt="Benicio Del Toro" title="Benicio Del Toro" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMTkzODQ4NzU1N15BMl5BanBnXkFtZTcwOTUzMzc5Mg@@._V1_UY44_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm0001125/?ref_=ttfc_fc_cl_t26"> Benicio Del Toro
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            The Collector 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0000982/?ref_=ttfc_fc_cl_i27"><img height="44" width="32" alt="Josh Brolin" title="Josh Brolin" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMTQ1MzYyMjQ0Nl5BMl5BanBnXkFtZTcwMTA0ODkyMg@@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm0000982/?ref_=ttfc_fc_cl_t27"> Josh Brolin
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0000982?ref_=ttfc_fc_cl_t27">Thanos</a> 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0695435/?ref_=ttfc_fc_cl_i28"><img height="44" width="32" alt="Chris Pratt" title="Chris Pratt" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BNzg3MTgwOTgzMV5BMl5BanBnXkFtZTgwODIxMTUwMjE@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm0695435/?ref_=ttfc_fc_cl_t28"> Chris Pratt
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0695435?ref_=ttfc_fc_cl_t28">Peter Quill</a> /  
            <a href="/title/tt4154756/characters/nm0695435?ref_=ttfc_fc_cl_t28">Star-Lord</a> 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0348231/?ref_=ttfc_fc_cl_i29"><img height="44" width="32" alt="Sean Gunn" title="Sean Gunn" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BNjZmMWE0N2UtYTc5Yi00OWY0LTk1MzAtMzgwNWM0OGU3MTc2XkEyXkFqcGdeQXVyMjQwMDg0Ng@@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm0348231/?ref_=ttfc_fc_cl_t29"> Sean Gunn
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            On-Set Rocket 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0000458/?ref_=ttfc_fc_cl_i30"><img height="44" width="32" alt="William Hurt" title="William Hurt" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMjEyNzA5MTUxN15BMl5BanBnXkFtZTcwMTU3ODQ3MQ@@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm0000458/?ref_=ttfc_fc_cl_t30"> William Hurt
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0000458?ref_=ttfc_fc_cl_t30">Secretary of State Thaddeus Ross</a> 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm4004793/?ref_=ttfc_fc_cl_i31"><img height="44" width="32" alt="Letitia Wright" title="Letitia Wright" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMjIyMzgxMzc5N15BMl5BanBnXkFtZTgwNDg3NzYzMDI@._V1_UY44_CR5,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm4004793/?ref_=ttfc_fc_cl_t31"> Letitia Wright
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm4004793?ref_=ttfc_fc_cl_t31">Shuri</a> 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm1024953/?ref_=ttfc_fc_cl_i32"><img height="44" width="32" alt="Terry Notary" title="Terry Notary" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMTU5NzAxODU5NV5BMl5BanBnXkFtZTcwMTU0NDEzNg@@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm1024953/?ref_=ttfc_fc_cl_t32"> Terry Notary
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm1024953?ref_=ttfc_fc_cl_t32">Cull Obsidian</a> /  
            <a href="/title/tt4154756/characters/nm1024953?ref_=ttfc_fc_cl_t32">On-Set Groot</a> 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm2534167/?ref_=ttfc_fc_cl_i33"><img height="44" width="32" alt="Tom Vaughan-Lawlor" title="Tom Vaughan-Lawlor" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BNTQ3NTRiYzMtMGFhZC00OTlkLTlkOTMtZDc5OWMzMmJjNWVjXkEyXkFqcGdeQXVyNDkxMDg2MTk@._V1_UY44_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm2534167/?ref_=ttfc_fc_cl_t33"> Tom Vaughan-Lawlor
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm2534167?ref_=ttfc_fc_cl_t33">Ebony Maw</a> 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm4689420/?ref_=ttfc_fc_cl_i34"><img height="44" width="32" alt="Carrie Coon" title="Carrie Coon" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMTk1ODEzMTAyNF5BMl5BanBnXkFtZTgwNDExMTY5MTI@._V1_UY44_CR13,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm4689420/?ref_=ttfc_fc_cl_t34"> Carrie Coon
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm4689420?ref_=ttfc_fc_cl_t34">Proxima Midnight</a> 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm4473692/?ref_=ttfc_fc_cl_i35"><img height="44" width="32" alt="Michael James Shaw" title="Michael James Shaw" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BZDk1ZjViMTItOTZjOS00YmY1LWE3ZjItYjdhNmMxZTIzZmUxXkEyXkFqcGdeQXVyMzQ1NDYxNDY@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm4473692/?ref_=ttfc_fc_cl_t35"> Michael James Shaw
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm4473692?ref_=ttfc_fc_cl_t35">Corvus Glaive</a> 
  
  
  (as Michael Shaw)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0498278/?ref_=ttfc_fc_cl_i36"><img height="44" width="32" alt="Stan Lee" title="Stan Lee" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMTk3NDE3Njc5M15BMl5BanBnXkFtZTYwOTY5Nzc1._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm0498278/?ref_=ttfc_fc_cl_t36"> Stan Lee
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0498278?ref_=ttfc_fc_cl_t36">Bus Driver</a> 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm6328300/?ref_=ttfc_fc_cl_i37"><img height="44" width="32" alt="Winston Duke" title="Winston Duke" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMzc5ZjRhNTItMTM5MS00ZDIxLTk4MzYtYzZkZDBhMjE1ZjMwXkEyXkFqcGdeQXVyNTEwNTA1Njg@._V1_UY44_CR10,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm6328300/?ref_=ttfc_fc_cl_t37"> Winston Duke
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm6328300?ref_=ttfc_fc_cl_t37">M'Baku</a> 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0441042/?ref_=ttfc_fc_cl_i38"><img height="44" width="32" alt="Florence Kasumba" title="Florence Kasumba" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BYmQ1MjU0MjEtMzgxOC00ZDdlLWFjNjgtYjJhOTM4OWZiZGM4XkEyXkFqcGdeQXVyNDU5ODk2OTg@._V1_UY44_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm0441042/?ref_=ttfc_fc_cl_t38"> Florence Kasumba
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0441042?ref_=ttfc_fc_cl_t38">Ayo</a> 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0174403/?ref_=ttfc_fc_cl_i39"><img height="44" width="32" alt="Kerry Condon" title="Kerry Condon" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMTY5NjgyNDU3OV5BMl5BanBnXkFtZTgwNzA4NDczNjE@._V1_UY44_CR1,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm0174403/?ref_=ttfc_fc_cl_t39"> Kerry Condon
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Friday 
  
  
  (voice)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm1244650/?ref_=ttfc_fc_cl_i40"><img height="44" width="32" alt="Monique Ganderton" title="Monique Ganderton" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BNTJjM2ZhNjQtZjFlMi00N2Y4LThlYmYtNjI4ODc4NjhhZDY3XkEyXkFqcGdeQXVyMzUxMjQ5NA@@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm1244650/?ref_=ttfc_fc_cl_t40"> Monique Ganderton
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm1244650?ref_=ttfc_fc_cl_t40">On-Set Proxima Midnight</a> 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm8188622/?ref_=ttfc_fc_cl_i41"><img height="44" width="32" alt="Jacob Batalon" title="Jacob Batalon" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMTJiYzBlYTUtNTFhNy00YWJhLWIyODItMTQyMjM3ZTNiODY0XkEyXkFqcGdeQXVyMTA1MTQ2ODk1._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm8188622/?ref_=ttfc_fc_cl_t41"> Jacob Batalon
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm8188622?ref_=ttfc_fc_cl_t41">Ned</a> 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm2556904/?ref_=ttfc_fc_cl_i42"><img height="44" width="32" alt="Tiffany Espensen" title="Tiffany Espensen" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMjQ5MTI0MjktMGI4MS00ODM0LWIwZDctNGYxNTVjNDEyZDc0XkEyXkFqcGdeQXVyNDQxNjcxNQ@@._V1_UY44_CR7,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm2556904/?ref_=ttfc_fc_cl_t42"> Tiffany Espensen
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Cindy 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm4194645/?ref_=ttfc_fc_cl_i43"><img height="44" width="32" alt="Isabella Amara" title="Isabella Amara" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMTY1OWU1OGYtYTIyMC00YzU1LWIyYTMtOWE0ZjdlMjhiZDE3L2ltYWdlXkEyXkFqcGdeQXVyMjQ3MjI0MDA@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm4194645/?ref_=ttfc_fc_cl_t43"> Isabella Amara
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Sally 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm3219917/?ref_=ttfc_fc_cl_i44"><img height="44" width="32" alt="Ethan Dizon" title="Ethan Dizon" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMjA2MjQ2MzE4Nl5BMl5BanBnXkFtZTgwMzAyOTE3NjE@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm3219917/?ref_=ttfc_fc_cl_t44"> Ethan Dizon
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Tiny 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm7567556/?ref_=ttfc_fc_cl_i45"><img height="44" width="32" alt="Ariana Greenblatt" title="Ariana Greenblatt" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BNTNiNTVlY2QtNjUyMi00YWI5LWI0MmQtOTVlNGM0ZTE2MjhhXkEyXkFqcGdeQXVyNDM1NjQzOQ@@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm7567556/?ref_=ttfc_fc_cl_t45"> Ariana Greenblatt
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm7567556?ref_=ttfc_fc_cl_t45">Young Gamora</a> 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0438188/?ref_=ttfc_fc_cl_i46"><img height="44" width="32" alt="Ameenah Kaplan" title="Ameenah Kaplan" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BZTg1MTYwNDEtMmUzOS00ZTgyLTkyNjYtZGU3YzBiZWY3ZjI2XkEyXkFqcGdeQXVyMjYxMzAxNzU@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm0438188/?ref_=ttfc_fc_cl_t46"> Ameenah Kaplan
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0438188?ref_=ttfc_fc_cl_t46">Gamora's Mother</a> 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm2739851/?ref_=ttfc_fc_cl_i47"><img height="44" width="32" alt="Ross Marquand" title="Ross Marquand" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMDcyNWUxMDQtMGExOS00ZmVlLTgzZDUtMjk4MzI3NTkwMjgzXkEyXkFqcGdeQXVyMTIxNjMwNDM@._V1_UY44_CR1,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm2739851/?ref_=ttfc_fc_cl_t47"> Ross Marquand
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm2739851?ref_=ttfc_fc_cl_t47">Red Skull (Stonekeeper)</a> 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm3631621/?ref_=ttfc_fc_cl_i48"><img height="44" width="32" alt="Michael Anthony Rogers" title="Michael Anthony Rogers" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm3631621/?ref_=ttfc_fc_cl_t48"> Michael Anthony Rogers
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Secretary Ross' Aide 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm1321656/?ref_=ttfc_fc_cl_i49"><img height="44" width="32" alt="Stephen McFeely" title="Stephen McFeely" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BZmJlZTFkOTAtYTY0Yi00NjIxLTllYWQtNDgwN2RhY2VlNGVmXkEyXkFqcGdeQXVyNzY1ODU1OTk@._V1_UY44_CR1,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm1321656/?ref_=ttfc_fc_cl_t49"> Stephen McFeely
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Secretary Ross' Aide 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm1594381/?ref_=ttfc_fc_cl_i50"><img height="44" width="32" alt="Aaron Lazar" title="Aaron Lazar" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BYTE1M2Y0ZjUtOThlMy00ZDFjLWIyZmUtN2I0MjMwMjcxOWVhL2ltYWdlXkEyXkFqcGdeQXVyMTExNzAwMTQ@._V1_UY44_CR1,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm1594381/?ref_=ttfc_fc_cl_t50"> Aaron Lazar
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Doctor Strange Double 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm1128418/?ref_=ttfc_fc_cl_i51"><img height="44" width="32" alt="Robert Pralgo" title="Robert Pralgo" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMjIxNzc3NTg0Nl5BMl5BanBnXkFtZTgwNDg5MDYwNDE@._V1_UY44_CR17,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm1128418/?ref_=ttfc_fc_cl_t51"> Robert Pralgo
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Thanos Reader 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm8637369/?ref_=ttfc_fc_cl_i52"><img height="44" width="32" alt="Olaniyan Thurmon" title="Olaniyan Thurmon" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BNjg4ODhiYmUtZTVkMS00Y2EwLWEwM2EtOTczNmNkMThlNmRmXkEyXkFqcGdeQXVyOTc2NjAyOTA@._V1_UY44_CR6,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm8637369/?ref_=ttfc_fc_cl_t52"> Olaniyan Thurmon
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Teenage Groot Reader 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm3138500/?ref_=ttfc_fc_cl_i53"><img height="44" width="32" alt="Blair Jasin" title="Blair Jasin" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BODEzZTUyODQtNjE3My00MTgyLWFkMjEtNDQ0MTExMzU0YWFhXkEyXkFqcGdeQXVyMTk5NTc3Mzc@._V1_UY44_CR23,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm3138500/?ref_=ttfc_fc_cl_t53"> Blair Jasin
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Street Pedestrian #1 
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm2832703/?ref_=ttfc_fc_cl_i54"><img height="44" width="32" alt="Matthew Zuk" title="Matthew Zuk" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BNjg3MjExNzk1MF5BMl5BanBnXkFtZTgwOTQxNTA1ODE@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm2832703/?ref_=ttfc_fc_cl_t54"> Matthew Zuk
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Street Pedestrian #2 
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm9799191/?ref_=ttfc_fc_cl_i55"><img height="44" width="32" alt="Laura Miller" title="Laura Miller" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm9799191/?ref_=ttfc_fc_cl_t55"> Laura Miller
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Scottish News (STV) Reporter 
                  
          </td>
      </tr>
  <tr><td colspan="4" class="castlist_label">Rest of cast listed alphabetically:</td></tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm6112965/?ref_=ttfc_fc_cl_i56"><img height="44" width="32" alt="Marija Juliette Abney" title="Marija Juliette Abney" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BNTFiMTdmZDEtMjI3Zi00MGQ3LTlkMjItNTAwZjcwNzIyMTBjXkEyXkFqcGdeQXVyODQzMjc2MTA@._V1_UY44_CR9,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm6112965/?ref_=ttfc_fc_cl_t56"> Marija Juliette Abney
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm6112965?ref_=ttfc_fc_cl_t56">Dora Milaje</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm3821861/?ref_=ttfc_fc_cl_i57"><img height="44" width="32" alt="Janeshia Adams-Ginyard" title="Janeshia Adams-Ginyard" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BZDBhOTVjMzMtYTFjMS00MjcxLTlhZGYtNmVhODBlYmRhNjkwXkEyXkFqcGdeQXVyNDMyNzc4MjY@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm3821861/?ref_=ttfc_fc_cl_t57"> Janeshia Adams-Ginyard
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm3821861?ref_=ttfc_fc_cl_t57">Dora Milaje</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm3699149/?ref_=ttfc_fc_cl_i58"><img height="44" width="32" alt="Gee Alexander" title="Gee Alexander" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMTU3NzQzMzQ2Ml5BMl5BanBnXkFtZTgwODY4ODA0OTE@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm3699149/?ref_=ttfc_fc_cl_t58"> Gee Alexander
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm3699149?ref_=ttfc_fc_cl_t58">Kingsguard</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm7687715/?ref_=ttfc_fc_cl_i59"><img height="44" width="32" alt="Branden Arnold" title="Branden Arnold" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm7687715/?ref_=ttfc_fc_cl_t59"> Branden Arnold
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm7687715?ref_=ttfc_fc_cl_t59">Black Border Tribe</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0000110/?ref_=ttfc_fc_cl_i60"><img height="44" width="32" alt="Kenneth Branagh" title="Kenneth Branagh" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMjI0NTQ4Mjk5Ml5BMl5BanBnXkFtZTcwMDc1NjkzNw@@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm0000110/?ref_=ttfc_fc_cl_t60"> Kenneth Branagh
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0000110?ref_=ttfc_fc_cl_t60">Asgardian Distress Call</a> 
  
  
  (voice) (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm8152145/?ref_=ttfc_fc_cl_i61"><img height="44" width="32" alt="Sergio Briones" title="Sergio Briones" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BZjUxMTc3ODQtNTBjZC00Y2M0LTk0NzYtODFkOGMzN2NjMzI3XkEyXkFqcGdeQXVyNTYxNzM0NzY@._V1_UY44_CR6,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm8152145/?ref_=ttfc_fc_cl_t61"> Sergio Briones
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            NYPD 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm1330195/?ref_=ttfc_fc_cl_i62"><img height="44" width="32" alt="Jwaundace Candece" title="Jwaundace Candece" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BOTFlNzBjNmUtYjQ2NC00OTNhLThkNzctNjE4NTExYWUxNDFhXkEyXkFqcGdeQXVyMjc2MjY3Ng@@._V1_UY44_CR1,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm1330195/?ref_=ttfc_fc_cl_t62"> Jwaundace Candece
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm1330195?ref_=ttfc_fc_cl_t62">Jabari Warrior</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm5355228/?ref_=ttfc_fc_cl_i63"><img height="44" width="32" alt="Donny Carrington" title="Donny Carrington" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BNjA0MzU4ZmEtNTM2YS00NTRlLWE4MjMtNzI0ZDhhN2Y5ZmE5XkEyXkFqcGdeQXVyNTM3MDYxMDI@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm5355228/?ref_=ttfc_fc_cl_t63"> Donny Carrington
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm5355228?ref_=ttfc_fc_cl_t63">Kingsguard</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm8336192/?ref_=ttfc_fc_cl_i64"><img height="44" width="32" alt="Lucie Carroll" title="Lucie Carroll" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BNGExYmNjN2QtNjdkZC00ZTZlLWIxMGYtNWI4OTYxMzViNjFkXkEyXkFqcGdeQXVyNjgyMTIyNDQ@._V1_UY44_CR1,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm8336192/?ref_=ttfc_fc_cl_t64"> Lucie Carroll
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Mourner 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm8067338/?ref_=ttfc_fc_cl_i65"><img height="44" width="32" alt="Jamel Chambers" title="Jamel Chambers" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMTkzOTY2NjQ2NV5BMl5BanBnXkFtZTgwOTc3MjgzMDI@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm8067338/?ref_=ttfc_fc_cl_t65"> Jamel Chambers
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Merchant 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm7665019/?ref_=ttfc_fc_cl_i66"><img height="44" width="32" alt="Matthew Christensen" title="Matthew Christensen" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMTgyMDM4ZmItMWIxMC00MzFhLTk4YzQtMzlhNWUxZGQ3NTRjXkEyXkFqcGdeQXVyMjQwMDg0Ng@@._V1_UY44_CR15,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm7665019/?ref_=ttfc_fc_cl_t66"> Matthew Christensen
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Student 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm5703979/?ref_=ttfc_fc_cl_i67"><img height="44" width="32" alt="Tye Claybrook Jr." title="Tye Claybrook Jr." src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BYmMxOTdkNzQtNDIwZi00NGY4LTg4ZmUtZDE0YWRhNjVjYzBlXkEyXkFqcGdeQXVyODIzNjMzNTk@._V1_UY44_CR3,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm5703979/?ref_=ttfc_fc_cl_t67"> Tye Claybrook Jr.
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm5703979?ref_=ttfc_fc_cl_t67">Border Tribe Warrior</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm0204952/?ref_=ttfc_fc_cl_i68"><img height="44" width="32" alt="Keith Splinter Davis" title="Keith Splinter Davis" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMDE4N2M0YWUtNjg5Mi00YzBkLTg0NmEtNGE1NDM1NGU4MThiXkEyXkFqcGdeQXVyMjQwMDg0Ng@@._V1_UY44_CR17,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm0204952/?ref_=ttfc_fc_cl_t68"> Keith Splinter Davis
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0204952?ref_=ttfc_fc_cl_t68">Kingsguard</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm8990660/?ref_=ttfc_fc_cl_i69"><img height="44" width="32" alt="Cory Dunson" title="Cory Dunson" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm8990660/?ref_=ttfc_fc_cl_t69"> Cory Dunson
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm8990660?ref_=ttfc_fc_cl_t69">Kingsguard</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm5851457/?ref_=ttfc_fc_cl_i70"><img height="44" width="32" alt="Jazzy Ellis" title="Jazzy Ellis" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BNDcyYzg1MmMtMjZjNy00OWUxLTkxNDUtYTljZDIyNGVkYjg2XkEyXkFqcGdeQXVyMjQwMDg0Ng@@._V1_UY44_CR17,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm5851457/?ref_=ttfc_fc_cl_t70"> Jazzy Ellis
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm5851457?ref_=ttfc_fc_cl_t70">Jabari Warrior</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm4509108/?ref_=ttfc_fc_cl_i71"><img height="44" width="32" alt="David Dman Escobar" title="David Dman Escobar" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm4509108/?ref_=ttfc_fc_cl_t71"> David Dman Escobar
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Taxi Cab Driver 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm2706921/?ref_=ttfc_fc_cl_i72"><img height="44" width="32" alt="Steven Essani" title="Steven Essani" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm2706921/?ref_=ttfc_fc_cl_t72"> Steven Essani
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Soldier 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm8609436/?ref_=ttfc_fc_cl_i73"><img height="44" width="32" alt="Jacob Evans" title="Jacob Evans" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm8609436/?ref_=ttfc_fc_cl_t73"> Jacob Evans
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            NYC Pedestrian 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm7687714/?ref_=ttfc_fc_cl_i74"><img height="44" width="32" alt="Simeon Freeman" title="Simeon Freeman" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm7687714/?ref_=ttfc_fc_cl_t74"> Simeon Freeman
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm7687714?ref_=ttfc_fc_cl_t74">Border Tribe Warrior</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm9974042/?ref_=ttfc_fc_cl_i75"><img height="44" width="32" alt="Dylan Gajai" title="Dylan Gajai" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm9974042/?ref_=ttfc_fc_cl_t75"> Dylan Gajai
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            NYC Pedestrian 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm7877420/?ref_=ttfc_fc_cl_i76"><img height="44" width="32" alt="Daniela Gaskie" title="Daniela Gaskie" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm7877420/?ref_=ttfc_fc_cl_t76"> Daniela Gaskie
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            National Guard 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm4771952/?ref_=ttfc_fc_cl_i77"><img height="44" width="32" alt="Martavious Gayles" title="Martavious Gayles" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm4771952/?ref_=ttfc_fc_cl_t77"> Martavious Gayles
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Construction Worker 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm8074962/?ref_=ttfc_fc_cl_i78"><img height="44" width="32" alt="John Gettier" title="John Gettier" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm8074962/?ref_=ttfc_fc_cl_t78"> John Gettier
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            NYPD 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm9548534/?ref_=ttfc_fc_cl_i79"><img height="44" width="32" alt="Jomahl Gildersleve" title="Jomahl Gildersleve" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm9548534/?ref_=ttfc_fc_cl_t79"> Jomahl Gildersleve
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm9548534?ref_=ttfc_fc_cl_t79">Border Tribe Warrior</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm7080280/?ref_=ttfc_fc_cl_i80"><img height="44" width="32" alt="Denisha Gillespie" title="Denisha Gillespie" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BYjA0OTRlYzktZWFiNS00NGQ4LWIzYzktZWZkNzhiNWM5ZTEwXkEyXkFqcGdeQXVyMjQwMDg0Ng@@._V1_UY44_CR17,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm7080280/?ref_=ttfc_fc_cl_t80"> Denisha Gillespie
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm7080280?ref_=ttfc_fc_cl_t80">Dora Milaje</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm4609643/?ref_=ttfc_fc_cl_i81"><img height="44" width="32" alt="Solomon Glave" title="Solomon Glave" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm4609643/?ref_=ttfc_fc_cl_t81"> Solomon Glave
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Coffee Shop Employee 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm7506655/?ref_=ttfc_fc_cl_i82"><img height="44" width="32" alt="Emelita T. Gonzalez" title="Emelita T. Gonzalez" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm7506655/?ref_=ttfc_fc_cl_t82"> Emelita T. Gonzalez
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Zen-Whoberi Elder 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm4417721/?ref_=ttfc_fc_cl_i83"><img height="44" width="32" alt="Daniel Graham" title="Daniel Graham" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm4417721/?ref_=ttfc_fc_cl_t83"> Daniel Graham
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm4417721?ref_=ttfc_fc_cl_t83">Border Tribe Warrior</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm1511653/?ref_=ttfc_fc_cl_i84"><img height="44" width="32" alt="Carlos Guity" title="Carlos Guity" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BNDM2ODAyMzU0NV5BMl5BanBnXkFtZTcwNzk4MTMzMQ@@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm1511653/?ref_=ttfc_fc_cl_t84"> Carlos Guity
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm1511653?ref_=ttfc_fc_cl_t84">Kingsguard</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm7076969/?ref_=ttfc_fc_cl_i85"><img height="44" width="32" alt="Dawit Gulilat" title="Dawit Gulilat" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm7076969/?ref_=ttfc_fc_cl_t85"> Dawit Gulilat
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm7076969?ref_=ttfc_fc_cl_t85">Border Tribe Warrior</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm8820193/?ref_=ttfc_fc_cl_i86"><img height="44" width="32" alt="Cecil M. Henry" title="Cecil M. Henry" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BYzhlNTc5ZTMtZjRhMy00N2VmLWFiNDgtNWM5MTJhNzkyODRmXkEyXkFqcGdeQXVyNzQ5MDcwMDM@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm8820193/?ref_=ttfc_fc_cl_t86"> Cecil M. Henry
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Patron in Vehicle 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm8580985/?ref_=ttfc_fc_cl_i87"><img height="44" width="32" alt="Bobby Hoskins" title="Bobby Hoskins" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BOWZlYjYzNTUtOWUzZi00NjhiLTg0ZmItYmY3YmU5YWZlZDM4XkEyXkFqcGdeQXVyMjQwMDg0Ng@@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm8580985/?ref_=ttfc_fc_cl_t87"> Bobby Hoskins
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Asgardian 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm4649996/?ref_=ttfc_fc_cl_i88"><img height="44" width="32" alt="Rabon Hutcherson" title="Rabon Hutcherson" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BZDFlZTJiN2ItMDUzMy00YmNmLTgyOWItODRhNmU5NDc5YTlhXkEyXkFqcGdeQXVyMjM0MTA4OTA@._V1_UY44_CR6,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm4649996/?ref_=ttfc_fc_cl_t88"> Rabon Hutcherson
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm4649996?ref_=ttfc_fc_cl_t88">Border Tribe</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm0000168/?ref_=ttfc_fc_cl_i89"><img height="44" width="32" alt="Samuel L. Jackson" title="Samuel L. Jackson" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMTQ1NTQwMTYxNl5BMl5BanBnXkFtZTYwMjA1MzY1._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm0000168/?ref_=ttfc_fc_cl_t89"> Samuel L. Jackson
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm0000168?ref_=ttfc_fc_cl_t89">Nick Fury</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm8377846/?ref_=ttfc_fc_cl_i90"><img height="44" width="32" alt="Bobby James" title="Bobby James" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BNWZlYWU1ZGYtODE1MC00MGYzLThmNDYtYTI5OWU2MmE3ZmUwXkEyXkFqcGdeQXVyOTQxMDQ2NTQ@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm8377846/?ref_=ttfc_fc_cl_t90"> Bobby James
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm8377846?ref_=ttfc_fc_cl_t90">Border Tribe</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm5545351/?ref_=ttfc_fc_cl_i91"><img height="44" width="32" alt="Floyd Anthony Johns Jr." title="Floyd Anthony Johns Jr." src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMTYxNDUxODMxM15BMl5BanBnXkFtZTgwNTc4MDYyOTE@._V1_UY44_CR17,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm5545351/?ref_=ttfc_fc_cl_t91"> Floyd Anthony Johns Jr.
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm5545351?ref_=ttfc_fc_cl_t91">Jabari Warrior</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm9374108/?ref_=ttfc_fc_cl_i92"><img height="44" width="32" alt="Devin Koehler" title="Devin Koehler" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm9374108/?ref_=ttfc_fc_cl_t92"> Devin Koehler
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            NYC Pedestrian 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm9201765/?ref_=ttfc_fc_cl_i93"><img height="44" width="32" alt="Demetri Landell" title="Demetri Landell" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm9201765/?ref_=ttfc_fc_cl_t93"> Demetri Landell
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Asgardian 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm9453496/?ref_=ttfc_fc_cl_i94"><img height="44" width="32" alt="Chase Ledgerwood" title="Chase Ledgerwood" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMjEyODM3Y2MtMzBiMC00MTAyLWFkODgtMmEwZWY4YWU5YjU0XkEyXkFqcGdeQXVyNTI5NjIyMw@@._V1_UY44_CR23,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm9453496/?ref_=ttfc_fc_cl_t94"> Chase Ledgerwood
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            NYC Pedestrian 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm9177465/?ref_=ttfc_fc_cl_i95"><img height="44" width="32" alt="Elgin Lee" title="Elgin Lee" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm9177465/?ref_=ttfc_fc_cl_t95"> Elgin Lee
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Pedestrian 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm9714768/?ref_=ttfc_fc_cl_i96"><img height="44" width="32" alt="Alejandro Lievano" title="Alejandro Lievano" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm9714768/?ref_=ttfc_fc_cl_t96"> Alejandro Lievano
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            NYC Pedestrian 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm9780464/?ref_=ttfc_fc_cl_i97"><img height="44" width="32" alt="Luke Maher" title="Luke Maher" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm9780464/?ref_=ttfc_fc_cl_t97"> Luke Maher
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Medical Assistant 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm9866652/?ref_=ttfc_fc_cl_i98"><img height="44" width="32" alt="Joe Maitland" title="Joe Maitland" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm9866652/?ref_=ttfc_fc_cl_t98"> Joe Maitland
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Edinburgh Pedestrian 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm5009680/?ref_=ttfc_fc_cl_i99"><img height="44" width="32" alt="Andrew S. McMillan" title="Andrew S. McMillan" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm5009680/?ref_=ttfc_fc_cl_t99"> Andrew S. McMillan
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Fleeing Pedestrian 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm9061391/?ref_=ttfc_fc_cl_i100"><img height="44" width="32" alt="Perla Middleton" title="Perla Middleton" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMTljMDczMDktZjhiZS00NDU2LTgyNDItYWE0MDcwZTFjNTA3XkEyXkFqcGdeQXVyNzczMDU0ODE@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm9061391/?ref_=ttfc_fc_cl_t100"> Perla Middleton
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Business Worker 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm3327628/?ref_=ttfc_fc_cl_i101"><img height="44" width="32" alt="Michael Pierino Miller" title="Michael Pierino Miller" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BYjU2MWJmNWItYmMwYi00NjZlLTkyYzEtZDUwNzA5NWQzMGU1XkEyXkFqcGdeQXVyMTQyNjY0Mzc@._V1_UY44_CR1,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm3327628/?ref_=ttfc_fc_cl_t101"> Michael Pierino Miller
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            NY Business Man 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm9597928/?ref_=ttfc_fc_cl_i102"><img height="44" width="32" alt="Frank David Monroe" title="Frank David Monroe" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BN2QwZjFmODktNDI2ZS00ZDAwLTg2MTktOWMyM2FmMDcxMWNmXkEyXkFqcGdeQXVyMjQwMDg0Ng@@._V1_UY44_CR6,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm9597928/?ref_=ttfc_fc_cl_t102"> Frank David Monroe
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm9597928?ref_=ttfc_fc_cl_t102">Border Tribe Warrior</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm4610530/?ref_=ttfc_fc_cl_i103"><img height="44" width="32" alt="Kevin Montgomery" title="Kevin Montgomery" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm4610530/?ref_=ttfc_fc_cl_t103"> Kevin Montgomery
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Student 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm6770059/?ref_=ttfc_fc_cl_i104"><img height="44" width="32" alt="Jared Moser" title="Jared Moser" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm6770059/?ref_=ttfc_fc_cl_t104"> Jared Moser
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            NYC Pedestrian 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm5719611/?ref_=ttfc_fc_cl_i105"><img height="44" width="32" alt="Marie Mouroum" title="Marie Mouroum" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BYjQ5ZTFmNWMtNmMwMi00MjFjLTg5MzUtNDcwY2JhZmQ5ODEwXkEyXkFqcGdeQXVyMjQwMDg0Ng@@._V1_UY44_CR6,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm5719611/?ref_=ttfc_fc_cl_t105"> Marie Mouroum
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm5719611?ref_=ttfc_fc_cl_t105">Dora Milaje</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm7149222/?ref_=ttfc_fc_cl_i106"><img height="44" width="32" alt="Harrison Osterfield" title="Harrison Osterfield" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BNjFlZWQyZDMtZDRhZS00YmI0LWEyOWUtNTAwY2U5MzFjZjRhXkEyXkFqcGdeQXVyMzUyNTMwOTk@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm7149222/?ref_=ttfc_fc_cl_t106"> Harrison Osterfield
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Boy on Bus 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm8791166/?ref_=ttfc_fc_cl_i107"><img height="44" width="32" alt="Edward Parker" title="Edward Parker" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm8791166/?ref_=ttfc_fc_cl_t107"> Edward Parker
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Construction Worker 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm7607949/?ref_=ttfc_fc_cl_i108"><img height="44" width="32" alt="Annie Pisapia" title="Annie Pisapia" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BYWQ2NzhkNzMtYzQ4ZS00OWM0LTljYzItMWE0NmI3YzA3ZWFjL2ltYWdlXkEyXkFqcGdeQXVyNjg3MzUwMjU@._V1_UY44_CR6,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm7607949/?ref_=ttfc_fc_cl_t108"> Annie Pisapia
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Pedestrian 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm9638697/?ref_=ttfc_fc_cl_i109"><img height="44" width="32" alt="Austin Rospert" title="Austin Rospert" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm9638697/?ref_=ttfc_fc_cl_t109"> Austin Rospert
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Pedestrian 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm7166432/?ref_=ttfc_fc_cl_i110"><img height="44" width="32" alt="James Siderits" title="James Siderits" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMWEyYzNmMDUtYzEwOC00YzE0LWE3ZDAtYmZiMzY3Zjk3ZDUxXkEyXkFqcGdeQXVyNTkwMjEwMDg@._V1_UY44_CR17,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm7166432/?ref_=ttfc_fc_cl_t110"> James Siderits
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            NYC Pedestrian 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm8220834/?ref_=ttfc_fc_cl_i111"><img height="44" width="32" alt="Matthew Excel Simmons" title="Matthew Excel Simmons" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BOThiODBkYmQtNGNkNy00NmQ4LThkMjktZGRmYTliNjRlZTFjXkEyXkFqcGdeQXVyNjc2MTY2MjU@._V1_UY44_CR1,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm8220834/?ref_=ttfc_fc_cl_t111"> Matthew Excel Simmons
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Asgardian 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm1130627/?ref_=ttfc_fc_cl_i112"><img height="44" width="32" alt="Cobie Smulders" title="Cobie Smulders" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BMTkzNTUyMTczM15BMl5BanBnXkFtZTcwMjMxNTM4Nw@@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm1130627/?ref_=ttfc_fc_cl_t112"> Cobie Smulders
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            <a href="/title/tt4154756/characters/nm1130627?ref_=ttfc_fc_cl_t112">Maria Hill</a> 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm9353030/?ref_=ttfc_fc_cl_i113"><img height="44" width="32" alt="Shawn South" title="Shawn South" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm9353030/?ref_=ttfc_fc_cl_t113"> Shawn South
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            NYC Pedestrian 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm4024141/?ref_=ttfc_fc_cl_i114"><img height="44" width="32" alt="James Sterling" title="James Sterling" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm4024141/?ref_=ttfc_fc_cl_t114"> James Sterling
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            NYC Pedestrian 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm7642761/?ref_=ttfc_fc_cl_i115"><img height="44" width="32" alt="Travis Thompson" title="Travis Thompson" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BOWI0OWVlZDgtMDY5ZS00ZGFiLTlhMDYtZWI3ODY5OTJlMTk0XkEyXkFqcGdeQXVyMjQwMDg0Ng@@._V1_UY44_CR3,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm7642761/?ref_=ttfc_fc_cl_t115"> Travis Thompson
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            New York Pedestrian 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm9990032/?ref_=ttfc_fc_cl_i116"><img height="44" width="32" alt="Robert Tinsley" title="Robert Tinsley" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BZjg5Mjk3MGUtZDhjOS00NDUzLWExM2MtNmYzZmU2NzgxODViXkEyXkFqcGdeQXVyOTA0MDA2ODE@._V1_UY44_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm9990032/?ref_=ttfc_fc_cl_t116"> Robert Tinsley
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Sanitation Worker 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm9068384/?ref_=ttfc_fc_cl_i117"><img height="44" width="32" alt="Laurel O Wagner" title="Laurel O Wagner" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class=""></a>          </td>
          <td>
<a href="/name/nm9068384/?ref_=ttfc_fc_cl_t117"> Laurel O Wagner
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            San Francisco Pedestrian 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm4914570/?ref_=ttfc_fc_cl_i118"><img height="44" width="32" alt="Tanya Wheelock" title="Tanya Wheelock" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BZTkzN2E1YmYtYmFjMy00NjZlLTg3MjUtMWU1YjkyMzhmMTcyXkEyXkFqcGdeQXVyOTM2ODgzNw@@._V1_UX32_CR0,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm4914570/?ref_=ttfc_fc_cl_t118"> Tanya Wheelock
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Washington Square Park Waitress https://www.imdb.com/title/tt0073195/?ref_=fn_al_tt_1
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="even">
          <td class="primary_photo">
<a href="/name/nm4367623/?ref_=ttfc_fc_cl_i119"><img height="44" width="32" alt="Kevin D Wilson" title="Kevin D Wilson" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BNmI2ODg1MzYtMmQyZS00Yjg0LWIwMmMtOGIyYTRlZDRhMTM1XkEyXkFqcGdeQXVyMTAxMTI3NjQ3._V1_UY44_CR6,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm4367623/?ref_=ttfc_fc_cl_t119"> Kevin D Wilson
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            Jogger 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
      <tr class="odd">
          <td class="primary_photo">
<a href="/name/nm7859644/?ref_=ttfc_fc_cl_i120"><img height="44" width="32" alt="Michael David Yuhl" title="Michael David Yuhl" src="https://m.media-amazon.com/images/G/01/imdb/images/nopicture/32x44/name-2138558783._CB470041625_.png" class="loadlate" loadlate="https://m.media-amazon.com/images/M/MV5BOTU1NDc3ZGQtOTcwOS00YTZlLWEyMzktZDljOTY3Y2UwNTBkXkEyXkFqcGdeQXVyNjQ5Nzc0MTQ@._V1_UY44_CR1,0,32,44_AL_.jpg"></a>          </td>
          <td>
<a href="/name/nm7859644/?ref_=ttfc_fc_cl_t120"> Michael David Yuhl
</a>          </td>
          <td class="ellipsis">
              ...
          </td>
          <td class="character">
            NYC Maintenance 
  
  
  (uncredited)
  
                  
          </td>
      </tr>
    </tbody></table>"""
    soup = bs(html_doc, 'html.parser')
    actor_table = soup.find_all('td', class_ = 'primary_photo' )
    actors = []
    #print(bs.get_text(actor_table[0].findNextSibling('td')))
    #adds every actor to a list
    for i in range(len(actor_table)):
        actors.append(bs.get_text(actor_table[i].findNextSibling('td')))
    #removes whitespace characters
    for i in range(len(actors)):
        actors[i] = actors[i].strip()
    #print(actors)    
    return actors
                   
        
        
if __name__ == "__main__":
    print(table_scrape("https://www.imdb.com/title/tt7349950/?ref_=nv_sr_1?ref_=nv_sr_1", False))
