from bs4 import BeautifulSoup as bs

movie_name = ''
# num = ['st','nd','rd','th']

fruit = '''
      <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2740&amp;view=2-Film%20Title-Alpha">Lawrence of Arabia</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=3827&amp;view=1-Nominee-Alpha">Sam Spiegel, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=035-19&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2748&amp;view=2-Film%20Title-Alpha">The Longest Day</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=3828&amp;view=1-Nominee-Alpha">Darryl F. Zanuck, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2751&amp;view=2-Film%20Title-Alpha">Meredith Willson&#39;s The Music Man</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=3829&amp;view=1-Nominee-Alpha">Morton Da Costa, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2752&amp;view=2-Film%20Title-Alpha">Mutiny on the Bounty</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=3830&amp;view=1-Nominee-Alpha">Aaron Rosenberg, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2741&amp;view=2-Film%20Title-Alpha">To Kill a Mockingbird</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=3831&amp;view=1-Nominee-Alpha">Alan J. Pakula, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=36&amp;view=3-Award%20Category-Chron">1963 (36th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=36&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2855&amp;view=2-Film%20Title-Alpha">America America</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=3945&amp;view=1-Nominee-Alpha">Elia Kazan, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2845&amp;view=2-Film%20Title-Alpha">Cleopatra</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=3946&amp;view=1-Nominee-Alpha">Walter Wanger, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2858&amp;view=2-Film%20Title-Alpha">How the West Was Won</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=3947&amp;view=1-Nominee-Alpha">Bernard Smith, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2847&amp;view=2-Film%20Title-Alpha">Lilies of the Field</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=3948&amp;view=1-Nominee-Alpha">Ralph Nelson, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2843&amp;view=2-Film%20Title-Alpha">Tom Jones</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=3949&amp;view=1-Nominee-Alpha">Tony Richardson, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=036-19&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=37&amp;view=3-Award%20Category-Chron">1964 (37th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=37&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2899&amp;view=2-Film%20Title-Alpha">Becket</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4120&amp;view=1-Nominee-Alpha">Hal B. Wallis, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2902&amp;view=2-Film%20Title-Alpha">Dr. Strangelove or: How I Learned to Stop Worrying and Love the Bomb</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4121&amp;view=1-Nominee-Alpha">Stanley Kubrick, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2906&amp;view=2-Film%20Title-Alpha">Mary Poppins</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4122&amp;view=1-Nominee-Alpha">Walt Disney and Bill Walsh, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2900&amp;view=2-Film%20Title-Alpha">My Fair Lady</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4123&amp;view=1-Nominee-Alpha">Jack L. Warner, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=037-19&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2901&amp;view=2-Film%20Title-Alpha">Zorba the Greek</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4124&amp;view=1-Nominee-Alpha">Michael Cacoyannis, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=38&amp;view=3-Award%20Category-Chron">1965 (38th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=38&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2965&amp;view=2-Film%20Title-Alpha">Darling</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4242&amp;view=1-Nominee-Alpha">Joseph Janni, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2963&amp;view=2-Film%20Title-Alpha">Doctor Zhivago</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4243&amp;view=1-Nominee-Alpha">Carlo Ponti, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2960&amp;view=2-Film%20Title-Alpha">Ship of Fools</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4244&amp;view=1-Nominee-Alpha">Stanley Kramer, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2964&amp;view=2-Film%20Title-Alpha">The Sound of Music</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4245&amp;view=1-Nominee-Alpha">Robert Wise, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=038-19&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2961&amp;view=2-Film%20Title-Alpha">A Thousand Clowns</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4246&amp;view=1-Nominee-Alpha">Fred Coe, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=39&amp;view=3-Award%20Category-Chron">1966 (39th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=39&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3010&amp;view=2-Film%20Title-Alpha">Alfie</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4368&amp;view=1-Nominee-Alpha">Lewis Gilbert, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3012&amp;view=2-Film%20Title-Alpha">A Man for All Seasons</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4369&amp;view=1-Nominee-Alpha">Fred Zinnemann, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=039-19&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3008&amp;view=2-Film%20Title-Alpha">The Russians Are Coming The Russians Are Coming</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4370&amp;view=1-Nominee-Alpha">Norman Jewison, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3011&amp;view=2-Film%20Title-Alpha">The Sand Pebbles</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4371&amp;view=1-Nominee-Alpha">Robert Wise, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3009&amp;view=2-Film%20Title-Alpha">Who&#39;s Afraid of Virginia Woolf?</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4372&amp;view=1-Nominee-Alpha">Ernest Lehman, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=40&amp;view=3-Award%20Category-Chron">1967 (40th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=40&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3060&amp;view=2-Film%20Title-Alpha">Bonnie and Clyde</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4477&amp;view=1-Nominee-Alpha">Warren Beatty, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2754&amp;view=2-Film%20Title-Alpha">Doctor Dolittle</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4478&amp;view=1-Nominee-Alpha">Arthur P. Jacobs, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3061&amp;view=2-Film%20Title-Alpha">The Graduate</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4479&amp;view=1-Nominee-Alpha">Lawrence Turman, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3064&amp;view=2-Film%20Title-Alpha">Guess Who&#39;s Coming to Dinner</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4480&amp;view=1-Nominee-Alpha">Stanley Kramer, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3063&amp;view=2-Film%20Title-Alpha">In the Heat of the Night</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4481&amp;view=1-Nominee-Alpha">Walter Mirisch, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=040-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=41&amp;view=3-Award%20Category-Chron">1968 (41st)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=41&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2800&amp;view=2-Film%20Title-Alpha">Funny Girl</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4586&amp;view=1-Nominee-Alpha">Ray Stark, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2793&amp;view=2-Film%20Title-Alpha">The Lion in Winter</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4587&amp;view=1-Nominee-Alpha">Martin Poll, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2792&amp;view=2-Film%20Title-Alpha">Oliver!</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4588&amp;view=1-Nominee-Alpha">John Woolf, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=041-17&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2801&amp;view=2-Film%20Title-Alpha">Rachel, Rachel</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4589&amp;view=1-Nominee-Alpha">Paul Newman, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3179&amp;view=2-Film%20Title-Alpha">Romeo and Juliet</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4585&amp;view=1-Nominee-Alpha">Anthony Havelock-Allan and John Brabourne, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=42&amp;view=3-Award%20Category-Chron">1969 (42nd)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=42&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3212&amp;view=2-Film%20Title-Alpha">Anne of the Thousand Days</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4699&amp;view=1-Nominee-Alpha">Hal B. Wallis, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3255&amp;view=2-Film%20Title-Alpha">Butch Cassidy and the Sundance Kid</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4700&amp;view=1-Nominee-Alpha">John Foreman, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3226&amp;view=2-Film%20Title-Alpha">Hello, Dolly!</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4701&amp;view=1-Nominee-Alpha">Ernest Lehman, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3213&amp;view=2-Film%20Title-Alpha">Midnight Cowboy</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4702&amp;view=1-Nominee-Alpha">Jerome Hellman, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=042-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3229&amp;view=2-Film%20Title-Alpha">Z</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4703&amp;view=1-Nominee-Alpha">Jacques Perrin and Hamed Rachedi, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=43&amp;view=3-Award%20Category-Chron">1970 (43rd)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=43&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3269&amp;view=2-Film%20Title-Alpha">Airport</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4805&amp;view=1-Nominee-Alpha">Ross Hunter, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3258&amp;view=2-Film%20Title-Alpha">Five Easy Pieces</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4806&amp;view=1-Nominee-Alpha">Bob Rafelson and Richard Wechsler, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3259&amp;view=2-Film%20Title-Alpha">Love Story</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4807&amp;view=1-Nominee-Alpha">Howard G. Minsky, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3270&amp;view=2-Film%20Title-Alpha">M*A*S*H</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4808&amp;view=1-Nominee-Alpha">Ingo Preminger, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3260&amp;view=2-Film%20Title-Alpha">Patton</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4809&amp;view=1-Nominee-Alpha">Frank McCarthy, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=043-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=44&amp;view=3-Award%20Category-Chron">1971 (44th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=44&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3326&amp;view=2-Film%20Title-Alpha">A Clockwork Orange</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4912&amp;view=1-Nominee-Alpha">Stanley Kubrick, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3311&amp;view=2-Film%20Title-Alpha">Fiddler on the Roof</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4913&amp;view=1-Nominee-Alpha">Norman Jewison, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3308&amp;view=2-Film%20Title-Alpha">The French Connection</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4914&amp;view=1-Nominee-Alpha">Philip D&#39;Antoni, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=044-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3312&amp;view=2-Film%20Title-Alpha">The Last Picture Show</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4915&amp;view=1-Nominee-Alpha">Stephen J. Friedman, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3317&amp;view=2-Film%20Title-Alpha">Nicholas and Alexandra</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=4916&amp;view=1-Nominee-Alpha">Sam Spiegel, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=45&amp;view=3-Award%20Category-Chron">1972 (45th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=45&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3360&amp;view=2-Film%20Title-Alpha">Cabaret</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5015&amp;view=1-Nominee-Alpha">Cy Feuer, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3369&amp;view=2-Film%20Title-Alpha">Deliverance</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5016&amp;view=1-Nominee-Alpha">John Boorman, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3338&amp;view=2-Film%20Title-Alpha">The Emigrants</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5017&amp;view=1-Nominee-Alpha">Bengt Forslund, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3355&amp;view=2-Film%20Title-Alpha">The Godfather</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5018&amp;view=1-Nominee-Alpha">Albert S. Ruddy, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=045-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3358&amp;view=2-Film%20Title-Alpha">Sounder</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5019&amp;view=1-Nominee-Alpha">Robert B. Radnitz, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=46&amp;view=3-Award%20Category-Chron">1973 (46th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=46&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3414&amp;view=2-Film%20Title-Alpha">American Graffiti</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5122&amp;view=1-Nominee-Alpha">Francis Ford Coppola, Producer;  Gary Kurtz, Co-Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3418&amp;view=2-Film%20Title-Alpha">Cries and Whispers</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5123&amp;view=1-Nominee-Alpha">Ingmar Bergman, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3409&amp;view=2-Film%20Title-Alpha">The Exorcist</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5124&amp;view=1-Nominee-Alpha">William Peter Blatty, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3406&amp;view=2-Film%20Title-Alpha">The Sting</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5125&amp;view=1-Nominee-Alpha">Tony Bill, Michael Phillips and Julia Phillips, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=046-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3410&amp;view=2-Film%20Title-Alpha">A Touch of Class</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5126&amp;view=1-Nominee-Alpha">Melvin Frank, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=47&amp;view=3-Award%20Category-Chron">1974 (47th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=47&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3451&amp;view=2-Film%20Title-Alpha">Chinatown</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5226&amp;view=1-Nominee-Alpha">Robert Evans, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3484&amp;view=2-Film%20Title-Alpha">The Conversation</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5227&amp;view=1-Nominee-Alpha">Francis Ford Coppola, Producer;  Fred Roos, Co-Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3452&amp;view=2-Film%20Title-Alpha">The Godfather Part II</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5228&amp;view=1-Nominee-Alpha">Francis Ford Coppola, Producer;  Gray Frederickson and Fred Roos, Co-Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=047-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3450&amp;view=2-Film%20Title-Alpha">Lenny</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5229&amp;view=1-Nominee-Alpha">Marvin Worth, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3453&amp;view=2-Film%20Title-Alpha">The Towering Inferno</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5230&amp;view=1-Nominee-Alpha">Irwin Allen, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=48&amp;view=3-Award%20Category-Chron">1975 (48th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=48&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3136&amp;view=2-Film%20Title-Alpha">Barry Lyndon</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5335&amp;view=1-Nominee-Alpha">Stanley Kubrick, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3124&amp;view=2-Film%20Title-Alpha">Dog Day Afternoon</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5336&amp;view=1-Nominee-Alpha">Martin Bregman and Martin Elfand, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3152&amp;view=2-Film%20Title-Alpha">Jaws</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5337&amp;view=1-Nominee-Alpha">Richard D. Zanuck and David Brown, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3133&amp;view=2-Film%20Title-Alpha">Nashville</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5338&amp;view=1-Nominee-Alpha">Robert Altman, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3123&amp;view=2-Film%20Title-Alpha">One Flew over the Cuckoo&#39;s Nest</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5339&amp;view=1-Nominee-Alpha">Saul Zaentz and Michael Douglas, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=048-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=49&amp;view=3-Award%20Category-Chron">1976 (49th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=49&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3735&amp;view=2-Film%20Title-Alpha">All the President&#39;s Men</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5446&amp;view=1-Nominee-Alpha">Walter Coblenz, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3744&amp;view=2-Film%20Title-Alpha">Bound for Glory</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5447&amp;view=1-Nominee-Alpha">Robert F. Blumofe and Harold Leventhal, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3177&amp;view=2-Film%20Title-Alpha">Network</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5448&amp;view=1-Nominee-Alpha">Howard Gottfried, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3733&amp;view=2-Film%20Title-Alpha">Rocky</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5449&amp;view=1-Nominee-Alpha">Irwin Winkler and Robert Chartoff, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=049-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3176&amp;view=2-Film%20Title-Alpha">Taxi Driver</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5450&amp;view=1-Nominee-Alpha">Michael Phillips and Julia Phillips, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=50&amp;view=3-Award%20Category-Chron">1977 (50th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=50&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3780&amp;view=2-Film%20Title-Alpha">Annie Hall</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5552&amp;view=1-Nominee-Alpha">Charles H. Joffe, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=050-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3782&amp;view=2-Film%20Title-Alpha">The Goodbye Girl</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5553&amp;view=1-Nominee-Alpha">Ray Stark, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3498&amp;view=2-Film%20Title-Alpha">Julia</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5554&amp;view=1-Nominee-Alpha">Richard Roth, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3786&amp;view=2-Film%20Title-Alpha">Star Wars</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5555&amp;view=1-Nominee-Alpha">Gary Kurtz, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3785&amp;view=2-Film%20Title-Alpha">The Turning Point</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5556&amp;view=1-Nominee-Alpha">Herbert Ross and Arthur Laurents, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=51&amp;view=3-Award%20Category-Chron">1978 (51st)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=51&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3075&amp;view=2-Film%20Title-Alpha">Coming Home</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5671&amp;view=1-Nominee-Alpha">Jerome Hellman, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3073&amp;view=2-Film%20Title-Alpha">The Deer Hunter</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5672&amp;view=1-Nominee-Alpha">Barry Spikings, Michael Deeley, Michael Cimino and John Peverall, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=051-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3071&amp;view=2-Film%20Title-Alpha">Heaven Can Wait</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5673&amp;view=1-Nominee-Alpha">Warren Beatty, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3077&amp;view=2-Film%20Title-Alpha">Midnight Express</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5674&amp;view=1-Nominee-Alpha">Alan Marshall and David Puttnam, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3080&amp;view=2-Film%20Title-Alpha">An Unmarried Woman</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5675&amp;view=1-Nominee-Alpha">Paul Mazursky and Tony Ray, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=52&amp;view=3-Award%20Category-Chron">1979 (52nd)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=52&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1567&amp;view=2-Film%20Title-Alpha">All That Jazz</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5785&amp;view=1-Nominee-Alpha">Robert Alan Aurthur, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1569&amp;view=2-Film%20Title-Alpha">Apocalypse Now</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5786&amp;view=1-Nominee-Alpha">Francis Coppola, Producer;  Fred Roos, Gray Frederickson and Tom Sternberg, Co-Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1575&amp;view=2-Film%20Title-Alpha">Breaking Away</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5787&amp;view=1-Nominee-Alpha">Peter Yates, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1564&amp;view=2-Film%20Title-Alpha">Kramer vs. Kramer</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5788&amp;view=1-Nominee-Alpha">Stanley R. Jaffe, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=052-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1573&amp;view=2-Film%20Title-Alpha">Norma Rae</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5789&amp;view=1-Nominee-Alpha">Tamara Asseyev and Alex Rose, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=53&amp;view=3-Award%20Category-Chron">1980 (53rd)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=53&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2322&amp;view=2-Film%20Title-Alpha">Coal Miner&#39;s Daughter</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5901&amp;view=1-Nominee-Alpha">Bernard Schwartz, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2314&amp;view=2-Film%20Title-Alpha">The Elephant Man</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5902&amp;view=1-Nominee-Alpha">Jonathan Sanger, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2317&amp;view=2-Film%20Title-Alpha">Ordinary People</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5903&amp;view=1-Nominee-Alpha">Ronald L. Schwary, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=053-15&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2312&amp;view=2-Film%20Title-Alpha">Raging Bull</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5904&amp;view=1-Nominee-Alpha">Irwin Winkler and Robert Chartoff, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2326&amp;view=2-Film%20Title-Alpha">Tess</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=5905&amp;view=1-Nominee-Alpha">Claude Berri, Producer;  Timothy Burrill, Co-Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=54&amp;view=3-Award%20Category-Chron">1981 (54th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=54&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1936&amp;view=2-Film%20Title-Alpha">Atlantic City</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6010&amp;view=1-Nominee-Alpha">Denis Heroux and John Kemeny, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1940&amp;view=2-Film%20Title-Alpha">Chariots of Fire</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6011&amp;view=1-Nominee-Alpha">David Puttnam, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=054-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1935&amp;view=2-Film%20Title-Alpha">On Golden Pond</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6012&amp;view=1-Nominee-Alpha">Bruce Gilbert, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1944&amp;view=2-Film%20Title-Alpha">Raiders of the Lost Ark</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6013&amp;view=1-Nominee-Alpha">Frank Marshall, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1934&amp;view=2-Film%20Title-Alpha">Reds</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6014&amp;view=1-Nominee-Alpha">Warren Beatty, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=55&amp;view=3-Award%20Category-Chron">1982 (55th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=55&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2064&amp;view=2-Film%20Title-Alpha">E.T. The Extra-Terrestrial</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6166&amp;view=1-Nominee-Alpha">Steven Spielberg and Kathleen Kennedy, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2050&amp;view=2-Film%20Title-Alpha">Gandhi</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6167&amp;view=1-Nominee-Alpha">Richard Attenborough, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=055-17&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2051&amp;view=2-Film%20Title-Alpha">Missing</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6168&amp;view=1-Nominee-Alpha">Edward Lewis and Mildred Lewis, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2049&amp;view=2-Film%20Title-Alpha">Tootsie</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6169&amp;view=1-Nominee-Alpha">Sydney Pollack and Dick Richards, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2052&amp;view=2-Film%20Title-Alpha">The Verdict</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6170&amp;view=1-Nominee-Alpha">Richard D. Zanuck and David Brown, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=56&amp;view=3-Award%20Category-Chron">1983 (56th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=56&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2104&amp;view=2-Film%20Title-Alpha">The Big Chill</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6282&amp;view=1-Nominee-Alpha">Michael Shamberg, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2096&amp;view=2-Film%20Title-Alpha">The Dresser</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6283&amp;view=1-Nominee-Alpha">Peter Yates, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2100&amp;view=2-Film%20Title-Alpha">The Right Stuff</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6284&amp;view=1-Nominee-Alpha">Irwin Winkler and Robert Chartoff, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2097&amp;view=2-Film%20Title-Alpha">Tender Mercies</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6285&amp;view=1-Nominee-Alpha">Philip S. Hobel, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2099&amp;view=2-Film%20Title-Alpha">Terms of Endearment</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6286&amp;view=1-Nominee-Alpha">James L. Brooks, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=056-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=57&amp;view=3-Award%20Category-Chron">1984 (57th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=57&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2140&amp;view=2-Film%20Title-Alpha">Amadeus</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6394&amp;view=1-Nominee-Alpha">Saul Zaentz, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=057-17&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2143&amp;view=2-Film%20Title-Alpha">The Killing Fields</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6395&amp;view=1-Nominee-Alpha">David Puttnam, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2148&amp;view=2-Film%20Title-Alpha">A Passage to India</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6396&amp;view=1-Nominee-Alpha">John Brabourne and Richard Goodwin, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2145&amp;view=2-Film%20Title-Alpha">Places in the Heart</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6397&amp;view=1-Nominee-Alpha">Arlene Donovan, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2144&amp;view=2-Film%20Title-Alpha">A Soldier&#39;s Story</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6398&amp;view=1-Nominee-Alpha">Norman Jewison, Ronald L. Schwary and Patrick Palmer, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=58&amp;view=3-Award%20Category-Chron">1985 (58th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=58&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2192&amp;view=2-Film%20Title-Alpha">The Color Purple</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6533&amp;view=1-Nominee-Alpha">Steven Spielberg, Kathleen Kennedy, Frank Marshall and Quincy Jones, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2235&amp;view=2-Film%20Title-Alpha">Kiss of the Spider Woman</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6534&amp;view=1-Nominee-Alpha">David Weisman, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2203&amp;view=2-Film%20Title-Alpha">Out of Africa</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6535&amp;view=1-Nominee-Alpha">Sydney Pollack, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=058-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2193&amp;view=2-Film%20Title-Alpha">Prizzi&#39;s Honor</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6536&amp;view=1-Nominee-Alpha">John Foreman, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2224&amp;view=2-Film%20Title-Alpha">Witness</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6537&amp;view=1-Nominee-Alpha">Edward S. Feldman, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=59&amp;view=3-Award%20Category-Chron">1986 (59th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=59&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2246&amp;view=2-Film%20Title-Alpha">Children of a Lesser God</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6643&amp;view=1-Nominee-Alpha">Burt Sugarman and Patrick Palmer, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2254&amp;view=2-Film%20Title-Alpha">Hannah and Her Sisters</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6644&amp;view=1-Nominee-Alpha">Robert Greenhut, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2261&amp;view=2-Film%20Title-Alpha">The Mission</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6645&amp;view=1-Nominee-Alpha">Fernando Ghia and David Puttnam, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2269&amp;view=2-Film%20Title-Alpha">Platoon</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6646&amp;view=1-Nominee-Alpha">Arnold Kopelson, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=059-17&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2271&amp;view=2-Film%20Title-Alpha">A Room with a View</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6647&amp;view=1-Nominee-Alpha">Ismail Merchant, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=60&amp;view=3-Award%20Category-Chron">1987 (60th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=60&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1976&amp;view=2-Film%20Title-Alpha">Broadcast News</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6756&amp;view=1-Nominee-Alpha">James L. Brooks, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1985&amp;view=2-Film%20Title-Alpha">Fatal Attraction</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6757&amp;view=1-Nominee-Alpha">Stanley R. Jaffe and Sherry Lansing, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1992&amp;view=2-Film%20Title-Alpha">Hope and Glory</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6758&amp;view=1-Nominee-Alpha">John Boorman, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1995&amp;view=2-Film%20Title-Alpha">The Last Emperor</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6759&amp;view=1-Nominee-Alpha">Jeremy Thomas, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=060-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2000&amp;view=2-Film%20Title-Alpha">Moonstruck</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6760&amp;view=1-Nominee-Alpha">Patrick Palmer and Norman Jewison, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=61&amp;view=3-Award%20Category-Chron">1988 (61st)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=61&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2398&amp;view=2-Film%20Title-Alpha">The Accidental Tourist</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6874&amp;view=1-Nominee-Alpha">Lawrence Kasdan, Charles Okun and Michael Grillo, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2410&amp;view=2-Film%20Title-Alpha">Dangerous Liaisons</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6875&amp;view=1-Nominee-Alpha">Norma Heyman and Hank Moonjean, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2422&amp;view=2-Film%20Title-Alpha">Mississippi Burning</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6876&amp;view=1-Nominee-Alpha">Frederick Zollo and Robert F. Colesberry, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2426&amp;view=2-Film%20Title-Alpha">Rain Man</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6877&amp;view=1-Nominee-Alpha">Mark Johnson, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=061-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2439&amp;view=2-Film%20Title-Alpha">Working Girl</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6878&amp;view=1-Nominee-Alpha">Douglas Wick, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=62&amp;view=3-Award%20Category-Chron">1989 (62nd)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=62&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2459&amp;view=2-Film%20Title-Alpha">Born on the Fourth of July</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6991&amp;view=1-Nominee-Alpha">A. Kitman Ho and Oliver Stone, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2467&amp;view=2-Film%20Title-Alpha">Dead Poets Society</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6992&amp;view=1-Nominee-Alpha">Steven Haft, Paul Junger Witt and Tony Thomas, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2469&amp;view=2-Film%20Title-Alpha">Driving Miss Daisy</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6993&amp;view=1-Nominee-Alpha">Richard D. Zanuck and Lili Fini Zanuck, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=062-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2473&amp;view=2-Film%20Title-Alpha">Field of Dreams</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6994&amp;view=1-Nominee-Alpha">Lawrence Gordon and Charles Gordon, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2483&amp;view=2-Film%20Title-Alpha">My Left Foot</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=6995&amp;view=1-Nominee-Alpha">Noel Pearson, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=63&amp;view=3-Award%20Category-Chron">1990 (63rd)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=63&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2505&amp;view=2-Film%20Title-Alpha">Awakenings</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7101&amp;view=1-Nominee-Alpha">Walter F. Parkes and Lawrence Lasker, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2509&amp;view=2-Film%20Title-Alpha">Dances With Wolves</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7102&amp;view=1-Nominee-Alpha">Jim Wilson and Kevin Costner, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=063-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2516&amp;view=2-Film%20Title-Alpha">Ghost</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7103&amp;view=1-Nominee-Alpha">Lisa Weinstein, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2517&amp;view=2-Film%20Title-Alpha">The Godfather, Part III</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7104&amp;view=1-Nominee-Alpha">Francis Ford Coppola, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2518&amp;view=2-Film%20Title-Alpha">Good Fellas</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7105&amp;view=1-Nominee-Alpha">Irwin Winkler, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=64&amp;view=3-Award%20Category-Chron">1991 (64th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=64&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2557&amp;view=2-Film%20Title-Alpha">Beauty and the Beast</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7225&amp;view=1-Nominee-Alpha">Don Hahn, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2559&amp;view=2-Film%20Title-Alpha">Bugsy</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7226&amp;view=1-Nominee-Alpha">Mark Johnson, Barry Levinson and Warren Beatty, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2574&amp;view=2-Film%20Title-Alpha">JFK</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7227&amp;view=1-Nominee-Alpha">A. Kitman Ho and Oliver Stone, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2578&amp;view=2-Film%20Title-Alpha">The Prince of Tides</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7228&amp;view=1-Nominee-Alpha">Barbra Streisand and Andrew Karsch, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2583&amp;view=2-Film%20Title-Alpha">The Silence of the Lambs</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7229&amp;view=1-Nominee-Alpha">Edward Saxon, Kenneth Utt and Ron Bozman, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=064-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=65&amp;view=3-Award%20Category-Chron">1992 (65th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=65&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2607&amp;view=2-Film%20Title-Alpha">The Crying Game</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7322&amp;view=1-Nominee-Alpha">Stephen Woolley, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2612&amp;view=2-Film%20Title-Alpha">A Few Good Men</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7323&amp;view=1-Nominee-Alpha">David Brown, Rob Reiner and Andrew Scheinman, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2614&amp;view=2-Film%20Title-Alpha">Howards End</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7324&amp;view=1-Nominee-Alpha">Ismail Merchant, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2632&amp;view=2-Film%20Title-Alpha">Scent of a Woman</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7325&amp;view=1-Nominee-Alpha">Martin Brest, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2636&amp;view=2-Film%20Title-Alpha">Unforgiven</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7326&amp;view=1-Nominee-Alpha">Clint Eastwood, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=065-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=66&amp;view=3-Award%20Category-Chron">1993 (66th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=66&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2666&amp;view=2-Film%20Title-Alpha">The Fugitive</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7445&amp;view=1-Nominee-Alpha">Arnold Kopelson, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2673&amp;view=2-Film%20Title-Alpha">In the Name of the Father</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7446&amp;view=1-Nominee-Alpha">Jim Sheridan, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2679&amp;view=2-Film%20Title-Alpha">The Piano</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7447&amp;view=1-Nominee-Alpha">Jan Chapman, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2681&amp;view=2-Film%20Title-Alpha">The Remains of the Day</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7448&amp;view=1-Nominee-Alpha">Mike Nichols, John Calley and Ismail Merchant, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=2683&amp;view=2-Film%20Title-Alpha">Schindler&#39;s List</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7449&amp;view=1-Nominee-Alpha">Steven Spielberg, Gerald R. Molen and Branko Lustig, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=066-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=67&amp;view=3-Award%20Category-Chron">1994 (67th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=67&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1866&amp;view=2-Film%20Title-Alpha">Forrest Gump</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7588&amp;view=1-Nominee-Alpha">Wendy Finerman, Steve Tisch and Steve Starkey, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=067-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1867&amp;view=2-Film%20Title-Alpha">Four Weddings and a Funeral</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7589&amp;view=1-Nominee-Alpha">Duncan Kenworthy, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1885&amp;view=2-Film%20Title-Alpha">Pulp Fiction</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7590&amp;view=1-Nominee-Alpha">Lawrence Bender, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1887&amp;view=2-Film%20Title-Alpha">Quiz Show</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7591&amp;view=1-Nominee-Alpha">Robert Redford, Michael Jacobs, Julian Krainin and Michael Nozik, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1889&amp;view=2-Film%20Title-Alpha">The Shawshank Redemption</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7592&amp;view=1-Nominee-Alpha">Niki Marvin, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=68&amp;view=3-Award%20Category-Chron">1995 (68th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=68&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1899&amp;view=2-Film%20Title-Alpha">Apollo 13</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7701&amp;view=1-Nominee-Alpha">Brian Grazer, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1900&amp;view=2-Film%20Title-Alpha">Babe</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7702&amp;view=1-Nominee-Alpha">George Miller, Doug Mitchell and Bill Miller, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=1529&amp;view=2-Film%20Title-Alpha">Braveheart</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7703&amp;view=1-Nominee-Alpha">Mel Gibson, Alan Ladd, Jr. and Bruce Davey, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=068-17&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3624&amp;view=2-Film%20Title-Alpha">The Postman (Il Postino)</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7704&amp;view=1-Nominee-Alpha">Mario Cecchi Gori, Vittorio Cecchi Gori and Gaetano Daniele, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3630&amp;view=2-Film%20Title-Alpha">Sense and Sensibility</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7705&amp;view=1-Nominee-Alpha">Lindsay Doran, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=69&amp;view=3-Award%20Category-Chron">1996 (69th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=69&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3656&amp;view=2-Film%20Title-Alpha">The English Patient</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7836&amp;view=1-Nominee-Alpha">Saul Zaentz, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=069-17&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3659&amp;view=2-Film%20Title-Alpha">Fargo</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7837&amp;view=1-Nominee-Alpha">Ethan Coen, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3668&amp;view=2-Film%20Title-Alpha">Jerry Maguire</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7838&amp;view=1-Nominee-Alpha">James L. Brooks, Laurence Mark, Richard Sakai and Cameron Crowe, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3683&amp;view=2-Film%20Title-Alpha">Secrets &amp; Lies</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7839&amp;view=1-Nominee-Alpha">Simon Channing-Williams, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3684&amp;view=2-Film%20Title-Alpha">Shine</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7840&amp;view=1-Nominee-Alpha">Jane Scott, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=70&amp;view=3-Award%20Category-Chron">1997 (70th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=70&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3730&amp;view=2-Film%20Title-Alpha">As Good as It Gets</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7961&amp;view=1-Nominee-Alpha">James L. Brooks, Bridget Johnson and Kristi Zea, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3530&amp;view=2-Film%20Title-Alpha">The Full Monty</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7962&amp;view=1-Nominee-Alpha">Uberto Pasolini, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3532&amp;view=2-Film%20Title-Alpha">Good Will Hunting</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7963&amp;view=1-Nominee-Alpha">Lawrence Bender, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3537&amp;view=2-Film%20Title-Alpha">L.A. Confidential</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7964&amp;view=1-Nominee-Alpha">Arnon Milchan, Curtis Hanson and Michael Nathanson, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3548&amp;view=2-Film%20Title-Alpha">Titanic</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=7965&amp;view=1-Nominee-Alpha">James Cameron and Jon Landau, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=070-17&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=71&amp;view=3-Award%20Category-Chron">1998 (71st)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=71&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3806&amp;view=2-Film%20Title-Alpha">Elizabeth</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=8091&amp;view=1-Nominee-Alpha">Alison Owen, Eric Fellner and Tim Bevan, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3814&amp;view=2-Film%20Title-Alpha">Life Is Beautiful</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=8092&amp;view=1-Nominee-Alpha">Elda Ferri and Gianluigi Braschi, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3827&amp;view=2-Film%20Title-Alpha">Saving Private Ryan</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=8093&amp;view=1-Nominee-Alpha">Steven Spielberg, Ian Bryce, Mark Gordon and Gary Levinsohn, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3828&amp;view=2-Film%20Title-Alpha">Shakespeare in Love</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=8094&amp;view=1-Nominee-Alpha">David Parfitt, Donna Gigliotti, Harvey Weinstein, Edward Zwick and Marc Norman, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=071-17&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3831&amp;view=2-Film%20Title-Alpha">The Thin Red Line</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=8095&amp;view=1-Nominee-Alpha">Robert Michael Geisler, John Roberdeau and Grant Hill, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=72&amp;view=3-Award%20Category-Chron">1999 (72nd)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=72&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3849&amp;view=2-Film%20Title-Alpha">American Beauty</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=8232&amp;view=1-Nominee-Alpha">Bruce Cohen and Dan Jinks, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=072-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3858&amp;view=2-Film%20Title-Alpha">The Cider House Rules</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=8233&amp;view=1-Nominee-Alpha">Richard N. Gladstein, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3865&amp;view=2-Film%20Title-Alpha">The Green Mile</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=8234&amp;view=1-Nominee-Alpha">David Valdes and Frank Darabont, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3867&amp;view=2-Film%20Title-Alpha">The Insider</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=8235&amp;view=1-Nominee-Alpha">Michael Mann and Pieter Jan Brugge, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3876&amp;view=2-Film%20Title-Alpha">The Sixth Sense</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=8236&amp;view=1-Nominee-Alpha">Frank Marshall, Kathleen Kennedy and Barry Mendel, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=73&amp;view=3-Award%20Category-Chron">2000 (73rd)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=73&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3899&amp;view=2-Film%20Title-Alpha">Chocolat</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=8354&amp;view=1-Nominee-Alpha">David Brown, Kit Golden and Leslie Holleran, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3901&amp;view=2-Film%20Title-Alpha">Crouching Tiger, Hidden Dragon</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=8355&amp;view=1-Nominee-Alpha">Bill Kong, Hsu Li Kong and Ang Lee, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3906&amp;view=2-Film%20Title-Alpha">Erin Brockovich</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=8356&amp;view=1-Nominee-Alpha">Danny DeVito, Michael Shamberg and Stacey Sher, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3908&amp;view=2-Film%20Title-Alpha">Gladiator</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=8357&amp;view=1-Nominee-Alpha">Douglas Wick, David Franzoni and Branko Lustig, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=073-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3927&amp;view=2-Film%20Title-Alpha">Traffic</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=8358&amp;view=1-Nominee-Alpha">Edward Zwick, Marshall Herskovitz and Laura Bickford, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=74&amp;view=3-Award%20Category-Chron">2001 (74th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=74&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3961&amp;view=2-Film%20Title-Alpha">A Beautiful Mind</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=8921&amp;view=1-Nominee-Alpha">Brian Grazer and Ron Howard, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=074-17&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3973&amp;view=2-Film%20Title-Alpha">Gosford Park</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=8922&amp;view=1-Nominee-Alpha">Robert Altman, Bob Balaban and David Levy, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3978&amp;view=2-Film%20Title-Alpha">In the Bedroom</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=8923&amp;view=1-Nominee-Alpha">Graham Leader, Ross Katz and Todd Field, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3986&amp;view=2-Film%20Title-Alpha">The Lord of the Rings: The Fellowship of the Ring</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=8924&amp;view=1-Nominee-Alpha">Peter Jackson, Fran Walsh and Barrie M. Osborne, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3992&amp;view=2-Film%20Title-Alpha">Moulin Rouge</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=8925&amp;view=1-Nominee-Alpha">Martin Brown, Baz Luhrmann and Fred Baron, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=75&amp;view=3-Award%20Category-Chron">2002 (75th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=75&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3518&amp;view=2-Film%20Title-Alpha">Chicago</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9038&amp;view=1-Nominee-Alpha">Martin Richards, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=075-17&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3583&amp;view=2-Film%20Title-Alpha">Gangs of New York</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9039&amp;view=1-Nominee-Alpha">Alberto Grimaldi and Harvey Weinstein, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3585&amp;view=2-Film%20Title-Alpha">The Hours</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9040&amp;view=1-Nominee-Alpha">Scott Rudin and Robert Fox, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3593&amp;view=2-Film%20Title-Alpha">The Lord of the Rings: The Two Towers</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9041&amp;view=1-Nominee-Alpha">Barrie M. Osborne, Fran Walsh and Peter Jackson, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=3603&amp;view=2-Film%20Title-Alpha">The Pianist</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9042&amp;view=1-Nominee-Alpha">Roman Polanski, Robert Benmussa and Alain Sarde, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=76&amp;view=3-Award%20Category-Chron">2003 (76th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=76&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4237&amp;view=2-Film%20Title-Alpha">The Lord of the Rings: The Return of the King</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9161&amp;view=1-Nominee-Alpha">Barrie M. Osborne, Peter Jackson and Fran Walsh, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=076-17&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4238&amp;view=2-Film%20Title-Alpha">Lost in Translation</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9162&amp;view=1-Nominee-Alpha">Ross Katz and Sofia Coppola, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4239&amp;view=2-Film%20Title-Alpha">Master and Commander: The Far Side of the World</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9163&amp;view=1-Nominee-Alpha">Samuel Goldwyn, Jr., Peter Weir and Duncan Henderson, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4244&amp;view=2-Film%20Title-Alpha">Mystic River</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9164&amp;view=1-Nominee-Alpha">Robert Lorenz, Judie G. Hoyt and Clint Eastwood, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4248&amp;view=2-Film%20Title-Alpha">Seabiscuit</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9165&amp;view=1-Nominee-Alpha">Kathleen Kennedy, Frank Marshall and Gary Ross, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=77&amp;view=3-Award%20Category-Chron">2004 (77th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=77&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4067&amp;view=2-Film%20Title-Alpha">The Aviator</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9273&amp;view=1-Nominee-Alpha">Michael Mann and Graham King, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4023&amp;view=2-Film%20Title-Alpha">Finding Neverland</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9274&amp;view=1-Nominee-Alpha">Richard N. Gladstein and Nellie Bellflower, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4031&amp;view=2-Film%20Title-Alpha">Million Dollar Baby</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9275&amp;view=1-Nominee-Alpha">Clint Eastwood, Albert S. Ruddy and Tom Rosenberg, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=077-17&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4035&amp;view=2-Film%20Title-Alpha">Ray</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9276&amp;view=1-Nominee-Alpha">Taylor Hackford, Stuart Benjamin and Howard Baldwin, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4039&amp;view=2-Film%20Title-Alpha">Sideways</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9277&amp;view=1-Nominee-Alpha">Michael London, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=78&amp;view=3-Award%20Category-Chron">2005 (78th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=78&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4133&amp;view=2-Film%20Title-Alpha">Brokeback Mountain</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9399&amp;view=1-Nominee-Alpha">Diana Ossana and James Schamus, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4134&amp;view=2-Film%20Title-Alpha">Capote</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9400&amp;view=1-Nominee-Alpha">Caroline Baron, William Vince and Michael Ohoven, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4140&amp;view=2-Film%20Title-Alpha">Crash</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9401&amp;view=1-Nominee-Alpha">Paul Haggis and Cathy Schulman, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=078-17&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4146&amp;view=2-Film%20Title-Alpha">Good Night, and Good Luck.</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9402&amp;view=1-Nominee-Alpha">Grant Heslov, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4141&amp;view=2-Film%20Title-Alpha">Munich</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9403&amp;view=1-Nominee-Alpha">Kathleen Kennedy, Steven Spielberg and Barry Mendel, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=79&amp;view=3-Award%20Category-Chron">2006 (79th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=79&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4082&amp;view=2-Film%20Title-Alpha">Babel</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9530&amp;view=1-Nominee-Alpha">Alejandro González Iñárritu, Jon Kilik and Steve Golin, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4095&amp;view=2-Film%20Title-Alpha">The Departed</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9531&amp;view=1-Nominee-Alpha">Graham King, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=079-17&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4110&amp;view=2-Film%20Title-Alpha">Letters from Iwo Jima</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9532&amp;view=1-Nominee-Alpha">Clint Eastwood, Steven Spielberg and Robert Lorenz, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4114&amp;view=2-Film%20Title-Alpha">Little Miss Sunshine</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9533&amp;view=1-Nominee-Alpha">David T. Friendly, Peter Saraf and Marc Turtletaub, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4042&amp;view=2-Film%20Title-Alpha">The Queen</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9534&amp;view=1-Nominee-Alpha">Andy Harries, Christine Langan and Tracey Seaward, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=80&amp;view=3-Award%20Category-Chron">2007 (80th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=80&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4296&amp;view=2-Film%20Title-Alpha">Atonement</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9660&amp;view=1-Nominee-Alpha">Tim Bevan, Eric Fellner and Paul Webster, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4312&amp;view=2-Film%20Title-Alpha">Juno</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9661&amp;view=1-Nominee-Alpha">Lianne Halfon, Mason Novick and Russell Smith, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4317&amp;view=2-Film%20Title-Alpha">Michael Clayton</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9662&amp;view=1-Nominee-Alpha">Sydney Pollack, Jennifer Fox and Kerry Orent, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4319&amp;view=2-Film%20Title-Alpha">No Country for Old Men</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9663&amp;view=1-Nominee-Alpha">Scott Rudin, Ethan Coen and Joel Coen, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=080-17&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4332&amp;view=2-Film%20Title-Alpha">There Will Be Blood</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9664&amp;view=1-Nominee-Alpha">JoAnne Sellar, Paul Thomas Anderson and Daniel Lupi, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=81&amp;view=3-Award%20Category-Chron">2008 (81st)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=81&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4208&amp;view=2-Film%20Title-Alpha">The Curious Case of Benjamin Button</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9785&amp;view=1-Nominee-Alpha">Kathleen Kennedy, Frank Marshall and Ceán Chaffin, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4041&amp;view=2-Film%20Title-Alpha">Frost/Nixon</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9786&amp;view=1-Nominee-Alpha">Brian Grazer, Ron Howard and Eric Fellner, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4055&amp;view=2-Film%20Title-Alpha">Milk</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9787&amp;view=1-Nominee-Alpha">Dan Jinks and Bruce Cohen, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4278&amp;view=2-Film%20Title-Alpha">The Reader</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9788&amp;view=1-Nominee-Alpha">Anthony Minghella, Sydney Pollack, Donna Gigliotti and Redmond Morris, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4281&amp;view=2-Film%20Title-Alpha">Slumdog Millionaire</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9789&amp;view=1-Nominee-Alpha">Christian Colson, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=081-17&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=82&amp;view=3-Award%20Category-Chron">2009 (82nd)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=82&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4337&amp;view=2-Film%20Title-Alpha">Avatar</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9908&amp;view=1-Nominee-Alpha">James Cameron and Jon Landau, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4338&amp;view=2-Film%20Title-Alpha">The Blind Side</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9909&amp;view=1-Nominee-Alpha">Gil Netter, Andrew A. Kosove and Broderick Johnson, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4346&amp;view=2-Film%20Title-Alpha">District 9</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9910&amp;view=1-Nominee-Alpha">Peter Jackson and Carolynne Cunningham, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4348&amp;view=2-Film%20Title-Alpha">An Education</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9911&amp;view=1-Nominee-Alpha">Finola Dwyer and Amanda Posey, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4354&amp;view=2-Film%20Title-Alpha">The Hurt Locker</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9912&amp;view=1-Nominee-Alpha">Kathryn Bigelow, Mark Boal, Nicolas Chartier and Greg Shapiro, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=082-17&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4358&amp;view=2-Film%20Title-Alpha">Inglourious Basterds</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9913&amp;view=1-Nominee-Alpha">Lawrence Bender, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4271&amp;view=2-Film%20Title-Alpha">Precious: Based on the Novel &#39;Push&#39; by Sapphire</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9914&amp;view=1-Nominee-Alpha">Lee Daniels, Sarah Siegel-Magness and Gary Magness, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4481&amp;view=2-Film%20Title-Alpha">A Serious Man</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9915&amp;view=1-Nominee-Alpha">Joel Coen and Ethan Coen, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4486&amp;view=2-Film%20Title-Alpha">Up</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9916&amp;view=1-Nominee-Alpha">Jonas Rivera, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4487&amp;view=2-Film%20Title-Alpha">Up in the Air</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=9917&amp;view=1-Nominee-Alpha">Daniel Dubiecki, Ivan Reitman and Jason Reitman, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=83&amp;view=3-Award%20Category-Chron">2010 (83rd)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=83&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4366&amp;view=2-Film%20Title-Alpha">Black Swan</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10045&amp;view=1-Nominee-Alpha">Mike Medavoy, Brian Oliver and Scott Franklin, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4374&amp;view=2-Film%20Title-Alpha">The Fighter</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10046&amp;view=1-Nominee-Alpha">David Hoberman, Todd Lieberman and Mark Wahlberg, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4402&amp;view=2-Film%20Title-Alpha">Inception</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10047&amp;view=1-Nominee-Alpha">Emma Thomas and Christopher Nolan, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4405&amp;view=2-Film%20Title-Alpha">The Kids Are All Right</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10048&amp;view=1-Nominee-Alpha">Gary Gilbert, Jeffrey Levy-Hinte and Celine Rattray, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4407&amp;view=2-Film%20Title-Alpha">The King&#39;s Speech</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10049&amp;view=1-Nominee-Alpha">Iain Canning, Emile Sherman and Gareth Unwin, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=083-17&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4412&amp;view=2-Film%20Title-Alpha">127 Hours</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10050&amp;view=1-Nominee-Alpha">Christian Colson, Danny Boyle and John Smithson, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4418&amp;view=2-Film%20Title-Alpha">The Social Network</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10051&amp;view=1-Nominee-Alpha">Scott Rudin, Dana Brunetti, Michael De Luca and Ceán Chaffin, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4424&amp;view=2-Film%20Title-Alpha">Toy Story 3</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10052&amp;view=1-Nominee-Alpha">Darla K. Anderson, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4426&amp;view=2-Film%20Title-Alpha">True Grit</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10053&amp;view=1-Nominee-Alpha">Scott Rudin, Ethan Coen and Joel Coen, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4431&amp;view=2-Film%20Title-Alpha">Winter&#39;s Bone</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10054&amp;view=1-Nominee-Alpha">Anne Rosellini and Alix Madigan-Yorkin, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=84&amp;view=3-Award%20Category-Chron">2011 (84th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=84&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4437&amp;view=2-Film%20Title-Alpha">The Artist</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10180&amp;view=1-Nominee-Alpha">Thomas Langmann, Producer</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=084-17&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4445&amp;view=2-Film%20Title-Alpha">The Descendants</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10181&amp;view=1-Nominee-Alpha">Jim Burke, Alexander Payne and Jim Taylor, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4448&amp;view=2-Film%20Title-Alpha">Extremely Loud &amp; Incredibly Close</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10182&amp;view=1-Nominee-Alpha">Scott Rudin, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4455&amp;view=2-Film%20Title-Alpha">The Help</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10183&amp;view=1-Nominee-Alpha">Brunson Green, Chris Columbus and Michael Barnathan, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4456&amp;view=2-Film%20Title-Alpha">Hugo</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10184&amp;view=1-Nominee-Alpha">Graham King and Martin Scorsese, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4466&amp;view=2-Film%20Title-Alpha">Midnight in Paris</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10185&amp;view=1-Nominee-Alpha">Letty Aronson and Stephen Tenenbaum, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4467&amp;view=2-Film%20Title-Alpha">Moneyball</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10186&amp;view=1-Nominee-Alpha">Michael De Luca, Rachael Horovitz and Brad Pitt, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4387&amp;view=2-Film%20Title-Alpha">The Tree of Life</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10187&amp;view=1-Nominee-Alpha">Sarah Green, Bill Pohlad, Dede Gardner and Grant Hill, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4392&amp;view=2-Film%20Title-Alpha">War Horse</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10188&amp;view=1-Nominee-Alpha">Steven Spielberg and Kathleen Kennedy, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=85&amp;view=3-Award%20Category-Chron">2012 (85th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=85&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4396&amp;view=2-Film%20Title-Alpha">Amour</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10310&amp;view=1-Nominee-Alpha">Margaret Menegoz, Stefan Arndt, Veit Heiduschka and Michael Katz, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4398&amp;view=2-Film%20Title-Alpha">Argo</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10311&amp;view=1-Nominee-Alpha">Grant Heslov, Ben Affleck and George Clooney, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=085-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4528&amp;view=2-Film%20Title-Alpha">Beasts of the Southern Wild</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10312&amp;view=1-Nominee-Alpha">Dan Janvey, Josh Penn and Michael Gottwald, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4534&amp;view=2-Film%20Title-Alpha">Django Unchained</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10313&amp;view=1-Nominee-Alpha">Stacey Sher, Reginald Hudlin and Pilar Savone, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4550&amp;view=2-Film%20Title-Alpha">Les Misérables</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10314&amp;view=1-Nominee-Alpha">Tim Bevan, Eric Fellner, Debra Hayward and Cameron Mackintosh, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4551&amp;view=2-Film%20Title-Alpha">Life of Pi</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10315&amp;view=1-Nominee-Alpha">Gil Netter, Ang Lee and David Womark, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4552&amp;view=2-Film%20Title-Alpha">Lincoln</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10316&amp;view=1-Nominee-Alpha">Steven Spielberg and Kathleen Kennedy, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4569&amp;view=2-Film%20Title-Alpha">Silver Linings Playbook</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10317&amp;view=1-Nominee-Alpha">Donna Gigliotti, Bruce Cohen and Jonathan Gordon, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4575&amp;view=2-Film%20Title-Alpha">Zero Dark Thirty</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10318&amp;view=1-Nominee-Alpha">Mark Boal, Kathryn Bigelow and Megan Ellison, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=86&amp;view=3-Award%20Category-Chron">2013 (86th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=86&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4515&amp;view=2-Film%20Title-Alpha">American Hustle</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10446&amp;view=1-Nominee-Alpha">Charles Roven, Richard Suckle, Megan Ellison and Jonathan Gordon, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4523&amp;view=2-Film%20Title-Alpha">Captain Phillips</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10447&amp;view=1-Nominee-Alpha">Scott Rudin, Dana Brunetti and Michael De Luca, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4576&amp;view=2-Film%20Title-Alpha">Dallas Buyers Club</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10448&amp;view=1-Nominee-Alpha">Robbie Brenner and Rachel Winter, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4585&amp;view=2-Film%20Title-Alpha">Gravity</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10449&amp;view=1-Nominee-Alpha">Alfonso Cuarón and David Heyman, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4589&amp;view=2-Film%20Title-Alpha">Her</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10450&amp;view=1-Nominee-Alpha">Megan Ellison, Spike Jonze and Vincent Landay, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4603&amp;view=2-Film%20Title-Alpha">Nebraska</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10451&amp;view=1-Nominee-Alpha">Albert Berger and Ron Yerxa, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4497&amp;view=2-Film%20Title-Alpha">Philomena</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10452&amp;view=1-Nominee-Alpha">Gabrielle Tana, Steve Coogan and Tracey Seaward, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4506&amp;view=2-Film%20Title-Alpha">12 Years a Slave</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10453&amp;view=1-Nominee-Alpha">Brad Pitt, Dede Gardner, Jeremy Kleiner, Steve McQueen and Anthony Katagas, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=086-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4510&amp;view=2-Film%20Title-Alpha">The Wolf of Wall Street</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10454&amp;view=1-Nominee-Alpha">Martin Scorsese, Leonardo DiCaprio, Joey McFarland and Emma Tillinger Koskoff, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=87&amp;view=3-Award%20Category-Chron">2014 (87th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=87&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4511&amp;view=2-Film%20Title-Alpha">American Sniper</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10593&amp;view=1-Nominee-Alpha">Clint Eastwood, Robert Lorenz, Andrew Lazar, Bradley Cooper and Peter Morgan, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4707&amp;view=2-Film%20Title-Alpha">Birdman or (The Unexpected Virtue of Ignorance)</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10594&amp;view=1-Nominee-Alpha">Alejandro G. Iñárritu, John Lesher and James W. Skotchdopole, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=087-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4710&amp;view=2-Film%20Title-Alpha">Boyhood</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10595&amp;view=1-Nominee-Alpha">Richard Linklater and Cathleen Sutherland, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4606&amp;view=2-Film%20Title-Alpha">The Grand Budapest Hotel</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10596&amp;view=1-Nominee-Alpha">Wes Anderson, Scott Rudin, Steven Rales and Jeremy Dawson, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4611&amp;view=2-Film%20Title-Alpha">The Imitation Game</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10597&amp;view=1-Nominee-Alpha">Nora Grossman, Ido Ostrowsky and Teddy Schwarzman, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4638&amp;view=2-Film%20Title-Alpha">Selma</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10598&amp;view=1-Nominee-Alpha">Christian Colson, Oprah Winfrey, Dede Gardner and Jeremy Kleiner, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4644&amp;view=2-Film%20Title-Alpha">The Theory of Everything</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10599&amp;view=1-Nominee-Alpha">Tim Bevan, Eric Fellner, Lisa Bruce and Anthony McCarten, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4649&amp;view=2-Film%20Title-Alpha">Whiplash</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10600&amp;view=1-Nominee-Alpha">Jason Blum, Helen Estabrook and David Lancaster, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=88&amp;view=3-Award%20Category-Chron">2015 (88th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=88&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4658&amp;view=2-Film%20Title-Alpha">The Big Short</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10740&amp;view=1-Nominee-Alpha">Brad Pitt, Dede Gardner and Jeremy Kleiner, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4661&amp;view=2-Film%20Title-Alpha">Bridge of Spies</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10741&amp;view=1-Nominee-Alpha">Steven Spielberg, Marc Platt and Kristie Macosko Krieger, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4662&amp;view=2-Film%20Title-Alpha">Brooklyn</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10742&amp;view=1-Nominee-Alpha">Finola Dwyer and Amanda Posey, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4683&amp;view=2-Film%20Title-Alpha">Mad Max: Fury Road</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10743&amp;view=1-Nominee-Alpha">Doug Mitchell and George Miller, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4684&amp;view=2-Film%20Title-Alpha">The Martian</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10744&amp;view=1-Nominee-Alpha">Simon Kinberg, Ridley Scott, Michael Schaefer and Mark Huffam, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4689&amp;view=2-Film%20Title-Alpha">The Revenant</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10745&amp;view=1-Nominee-Alpha">Arnon Milchan, Steve Golin, Alejandro G. Iñárritu, Mary Parent and Keith Redmon, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4690&amp;view=2-Film%20Title-Alpha">Room</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10746&amp;view=1-Nominee-Alpha">Ed Guiney, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4697&amp;view=2-Film%20Title-Alpha">Spotlight</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10747&amp;view=1-Nominee-Alpha">Michael Sugar, Steve Golin, Nicole Rocklin and Blye Pagon Faust, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=088-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=89&amp;view=3-Award%20Category-Chron">2016 (89th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=89&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4721&amp;view=2-Film%20Title-Alpha">Arrival</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10810&amp;view=1-Nominee-Alpha">Shawn Levy, Dan Levine, Aaron Ryder and David Linde, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4731&amp;view=2-Film%20Title-Alpha">Fences</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10829&amp;view=1-Nominee-Alpha">Scott Rudin, Denzel Washington and Todd Black, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4735&amp;view=2-Film%20Title-Alpha">Hacksaw Ridge</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10835&amp;view=1-Nominee-Alpha">Bill Mechanic and David Permut, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4737&amp;view=2-Film%20Title-Alpha">Hell or High Water</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10843&amp;view=1-Nominee-Alpha">Carla Hacken and Julie Yorn, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4738&amp;view=2-Film%20Title-Alpha">Hidden Figures</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10845&amp;view=1-Nominee-Alpha">Donna Gigliotti, Peter Chernin, Jenno Topping, Pharrell Williams and Theodore Melfi, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4746&amp;view=2-Film%20Title-Alpha">La La Land</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10895&amp;view=1-Nominee-Alpha">Fred Berger, Jordan Horowitz and Marc Platt, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4749&amp;view=2-Film%20Title-Alpha">Lion</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10898&amp;view=1-Nominee-Alpha">Emile Sherman, Iain Canning and Angie Fielder, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4753&amp;view=2-Film%20Title-Alpha">Manchester by the Sea</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10909&amp;view=1-Nominee-Alpha">Matt Damon, Kimberly Steward, Chris Moore, Lauren Beck and Kevin J. Walsh, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4755&amp;view=2-Film%20Title-Alpha">Moonlight</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10857&amp;view=1-Nominee-Alpha">Adele Romanski, Dede Gardner and Jeremy Kleiner, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=089-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=90&amp;view=3-Award%20Category-Chron">2017 (90th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=90&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4790&amp;view=2-Film%20Title-Alpha">Call Me by Your Name</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11032&amp;view=1-Nominee-Alpha">Peter Spears, Luca Guadagnino, Emilie Georges and Marco Morabito, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4792&amp;view=2-Film%20Title-Alpha">Darkest Hour</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11061&amp;view=1-Nominee-Alpha">Tim Bevan, Eric Fellner, Lisa Bruce, Anthony McCarten and Douglas Urbanski, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4796&amp;view=2-Film%20Title-Alpha">Dunkirk</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10978&amp;view=1-Nominee-Alpha">Emma Thomas and Christopher Nolan, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4804&amp;view=2-Film%20Title-Alpha">Get Out</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11054&amp;view=1-Nominee-Alpha">Sean McKittrick, Jason Blum, Edward H. Hamm Jr. and Jordan Peele, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4814&amp;view=2-Film%20Title-Alpha">Lady Bird</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11048&amp;view=1-Nominee-Alpha">Scott Rudin, Eli Bush and Evelyn O&#39;Neill, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4826&amp;view=2-Film%20Title-Alpha">Phantom Thread</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10995&amp;view=1-Nominee-Alpha">JoAnne Sellar, Paul Thomas Anderson, Megan Ellison and Daniel Lupi, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4827&amp;view=2-Film%20Title-Alpha">The Post</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10954&amp;view=1-Nominee-Alpha">Amy Pascal, Steven Spielberg and Kristie Macosko Krieger, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4830&amp;view=2-Film%20Title-Alpha">The Shape of Water</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10988&amp;view=1-Nominee-Alpha">Guillermo del Toro and J. Miles Dale, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=090-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4835&amp;view=2-Film%20Title-Alpha">Three Billboards outside Ebbing, Missouri</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=10984&amp;view=1-Nominee-Alpha">Graham Broadbent, Pete Czernin and Martin McDonagh, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=91&amp;view=3-Award%20Category-Chron">2018 (91st)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=91&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4846&amp;view=2-Film%20Title-Alpha">Black Panther</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11142&amp;view=1-Nominee-Alpha">Kevin Feige, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4848&amp;view=2-Film%20Title-Alpha">BlacKkKlansman</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11194&amp;view=1-Nominee-Alpha">Sean McKittrick, Jason Blum, Raymond Mansfield, Jordan Peele and Spike Lee, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4849&amp;view=2-Film%20Title-Alpha">Bohemian Rhapsody</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11130&amp;view=1-Nominee-Alpha">Graham King, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4858&amp;view=2-Film%20Title-Alpha">The Favourite</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11116&amp;view=1-Nominee-Alpha">Ceci Dempsey, Ed Guiney, Lee Magiday and Yorgos Lanthimos, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4862&amp;view=2-Film%20Title-Alpha">Green Book</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11137&amp;view=1-Nominee-Alpha">Jim Burke, Charles B. Wessler, Brian Currie, Peter Farrelly and Nick Vallelonga, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=091-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4884&amp;view=2-Film%20Title-Alpha">Roma</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11126&amp;view=1-Nominee-Alpha">Gabriela Rodríguez and Alfonso Cuarón, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4889&amp;view=2-Film%20Title-Alpha">A Star Is Born</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11110&amp;view=1-Nominee-Alpha">Bill Gerber, Bradley Cooper and Lynette Howell Taylor, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=4890&amp;view=2-Film%20Title-Alpha">Vice</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11120&amp;view=1-Nominee-Alpha">Dede Gardner, Jeremy Kleiner, Adam McKay and Kevin Messick, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=92&amp;view=3-Award%20Category-Chron">2019 (92nd)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=92&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5011&amp;view=2-Film%20Title-Alpha">Ford v Ferrari</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11296&amp;view=1-Nominee-Alpha">Peter Chernin, Jenno Topping and James Mangold, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5019&amp;view=2-Film%20Title-Alpha">The Irishman</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11276&amp;view=1-Nominee-Alpha">Martin Scorsese, Robert De Niro, Jane Rosenthal and Emma Tillinger Koskoff, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5020&amp;view=2-Film%20Title-Alpha">Jojo Rabbit</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11235&amp;view=1-Nominee-Alpha">Carthew Neal, Taika Waititi and Chelsea Winstanley, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5021&amp;view=2-Film%20Title-Alpha">Joker</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11331&amp;view=1-Nominee-Alpha">Todd Phillips, Bradley Cooper and Emma Tillinger Koskoff, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5031&amp;view=2-Film%20Title-Alpha">Little Women</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11226&amp;view=1-Nominee-Alpha">Amy Pascal, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5033&amp;view=2-Film%20Title-Alpha">Marriage Story</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11290&amp;view=1-Nominee-Alpha">Noah Baumbach and David Heyman, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5038&amp;view=2-Film%20Title-Alpha">1917</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11314&amp;view=1-Nominee-Alpha">Sam Mendes, Pippa Harris, Jayne-Ann Tenggren and Callum McDougall, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5039&amp;view=2-Film%20Title-Alpha">Once upon a Time...in Hollywood</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11241&amp;view=1-Nominee-Alpha">David Heyman, Shannon McIntosh and Quentin Tarantino, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5041&amp;view=2-Film%20Title-Alpha">Parasite</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11265&amp;view=1-Nominee-Alpha">Kwak Sin Ae and Bong Joon Ho, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=092-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=93&amp;view=3-Award%20Category-Chron">2020 (93rd)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=93&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5064&amp;view=2-Film%20Title-Alpha">The Father</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11390&amp;view=1-Nominee-Alpha">David Parfitt, Jean-Louis Livi and Philippe Carcassonne, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5071&amp;view=2-Film%20Title-Alpha">Judas and the Black Messiah</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11459&amp;view=1-Nominee-Alpha">Shaka King, Charles D. King and Ryan Coogler, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5078&amp;view=2-Film%20Title-Alpha">Mank</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11381&amp;view=1-Nominee-Alpha">Ceán Chaffin, Eric Roth and Douglas Urbanski, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5080&amp;view=2-Film%20Title-Alpha">Minari</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11385&amp;view=1-Nominee-Alpha">Christina Oh, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5085&amp;view=2-Film%20Title-Alpha">Nomadland</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11401&amp;view=1-Nominee-Alpha">Frances McDormand, Peter Spears, Mollye Asher, Dan Janvey and Chloé Zhao, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=093-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5094&amp;view=2-Film%20Title-Alpha">Promising Young Woman</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11375&amp;view=1-Nominee-Alpha">Ben Browning, Ashley Fox, Emerald Fennell and Josey McNamara, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5098&amp;view=2-Film%20Title-Alpha">Sound of Metal</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11377&amp;view=1-Nominee-Alpha">Bert Hamelinck and Sacha Ben Harroche, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5101&amp;view=2-Film%20Title-Alpha">The Trial of the Chicago 7</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11417&amp;view=1-Nominee-Alpha">Marc Platt and Stuart Besser, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=94&amp;view=3-Award%20Category-Chron">2021 (94th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=94&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5114&amp;view=2-Film%20Title-Alpha">Belfast</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11548&amp;view=1-Nominee-Alpha">Laura Berwick, Kenneth Branagh, Becca Kovacik and Tamar Thomas, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5117&amp;view=2-Film%20Title-Alpha">CODA</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11577&amp;view=1-Nominee-Alpha">Philippe Rousselet, Fabrice Gianfermi and Patrick Wachsberger, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=094-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5121&amp;view=2-Film%20Title-Alpha">Don&#39;t Look Up</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11487&amp;view=1-Nominee-Alpha">Adam McKay and Kevin Messick, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5123&amp;view=2-Film%20Title-Alpha">Drive My Car</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11597&amp;view=1-Nominee-Alpha">Teruhisa Yamamoto, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5124&amp;view=2-Film%20Title-Alpha">Dune</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11554&amp;view=1-Nominee-Alpha">Mary Parent, Denis Villeneuve and Cale Boyter, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5132&amp;view=2-Film%20Title-Alpha">King Richard</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11598&amp;view=1-Nominee-Alpha">Tim White, Trevor White and Will Smith, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5134&amp;view=2-Film%20Title-Alpha">Licorice Pizza</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11586&amp;view=1-Nominee-Alpha">Sara Murphy, Adam Somner and Paul Thomas Anderson, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5140&amp;view=2-Film%20Title-Alpha">Nightmare Alley</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11517&amp;view=1-Nominee-Alpha">Guillermo del Toro, J. Miles Dale and Bradley Cooper, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5145&amp;view=2-Film%20Title-Alpha">The Power of the Dog</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11525&amp;view=1-Nominee-Alpha">Jane Campion, Tanya Seghatchian, Emile Sherman, Iain Canning and Roger Frappier, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5156&amp;view=2-Film%20Title-Alpha">West Side Story</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11594&amp;view=1-Nominee-Alpha">Steven Spielberg and Kristie Macosko Krieger, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                    </div>
                            </div>                        
            </div>
        <div class="awards-result-chron result-group group-awardcategory-chron">                
                    <!--Show Year-->
                    <div class="result-group-header">
                        <div class="result-group-title">                            
                                <a class="nominations-link" href="/Search/Nominations?awardShowFrom=95&amp;view=3-Award%20Category-Chron">2022 (95th)</a>
                        </div>
                    </div>
                   
                            <div class="result-subgroup subgroup-awardcategory-chron">
                                <div class="result-subgroup-header">
                                    <!--Award Category Exact-->
                                    <div class="result-subgroup-title">
                                        <a class="nominations-link" href="/Search/Nominations?categoryExactId=55&amp;awardShowFrom=95&amp;view=3-Award%20Category-Chron">BEST PICTURE</a>
                                    </div>
                                </div>                                
                                <div class="awards-result-subgroup-items">                                    

                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5162&amp;view=2-Film%20Title-Alpha">All Quiet on the Western Front</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11686&amp;view=1-Nominee-Alpha">Malte Grunert, Producer</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5166&amp;view=2-Film%20Title-Alpha">Avatar: The Way of Water</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11667&amp;view=1-Nominee-Alpha">James Cameron and Jon Landau, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5168&amp;view=2-Film%20Title-Alpha">The Banshees of Inisherin</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11662&amp;view=1-Nominee-Alpha">Graham Broadbent, Pete Czernin and Martin McDonagh, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5178&amp;view=2-Film%20Title-Alpha">Elvis</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11631&amp;view=1-Nominee-Alpha">Baz Luhrmann, Catherine Martin, Gail Berman, Patrick McCormick and Schuyler Weiss, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                            <span class="glyphicon glyphicon-star" title="Winner"></span>
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5180&amp;view=2-Film%20Title-Alpha">Everything Everywhere All at Once</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11647&amp;view=1-Nominee-Alpha">Daniel Kwan, Daniel Scheinert and Jonathan Wang, Producers</a>
                                                            </div>
                                                            <div class="awards-result-speech">
                                                                <a class="awards-result-speech-link" onclick="window.open('http://aaspeechesdb.oscars.org/ics-wpd/url.ashx?id=095-16&amp;amp;qn=AAspeeches','name','width=1000,height=699')" target="popup">
                                                                    <span class="glyphicon glyphicon-comment" title="Acceptance Speech"></span>
                                                                </a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5181&amp;view=2-Film%20Title-Alpha">The Fabelmans</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11683&amp;view=1-Nominee-Alpha">Kristie Macosko Krieger, Steven Spielberg and Tony Kushner, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5207&amp;view=2-Film%20Title-Alpha">Tár</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11729&amp;view=1-Nominee-Alpha">Todd Field, Alexandra Milchan and Scott Lambert, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5210&amp;view=2-Film%20Title-Alpha">Top Gun: Maverick</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11731&amp;view=1-Nominee-Alpha">Tom Cruise, Christopher McQuarrie, David Ellison and Jerry Bruckheimer, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5211&amp;view=2-Film%20Title-Alpha">Triangle of Sadness</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11656&amp;view=1-Nominee-Alpha">Erik Hemmendorff and Philippe Bober, Producers</a>
                                                            </div>
                                                </div>
                                                </div>
                                                <div class="result-details awards-result-actingorsimilar">
                                                        <!--Acting or Similar-->
                                                <div class="awards-result-nomination awards-result-nomination-actingorsimilar">
                                                    
                                                            <div class="awards-result-film">
                                                                <div class="awards-result-film-title">
                                                                    <a class="nominations-link" href="/Search/Nominations?filmId=5214&amp;view=2-Film%20Title-Alpha">Women Talking</a>
                                                                </div>
                                                            </div>
                                                            <div class="awards-result-separator-hyphen">--</div>
                                                            <div class="awards-result-nominationstatement">
                                                                <a class="nominations-link" href="/Search/Nominations?nominationId=11652&amp;view=1-Nominee-Alpha">Dede Gardner, Jeremy Kleiner and Frances McDormand, Producers</a>
                                                            </div>
'''

root = bs(fruit, 'html.parser')
# print(root.prettify())

for each in root.find_all('a',{'class':'nominations-link'}):
    movie_name = movie_name + each.text + ' | '
    m_n_list = movie_name.split('|')
    while ' BEST PICTURE ' in m_n_list:
        m_n_list.remove(' BEST PICTURE ')
    for i in m_n_list:
        if 'Producers' in i:
            m_n_list.remove(i)
        elif 'Producer' in i:
            m_n_list.remove(i)
m_n_list.pop(421)
num =1
print(m_n_list)
for i in m_n_list:
    print(i)
    num +=1
print("Actual total: "+str(len(m_n_list)-60))

