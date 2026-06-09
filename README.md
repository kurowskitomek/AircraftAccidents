### **Cel projektu:**



Analiza wpływu modelu statku powietrznego na charakterystykę katastrof lotniczych w latach 1908–2019.



Badanie zostanie przeprowadzone na podstawie zbioru zawierającego m.in. model samolotu (AC Type), liczbę osób na pokładzie, liczbę ofiar śmiertelnych oraz opis przyczyn katastrofy. 





##### **Sposób wyboru modeli samolotów do analizy:**



Zbiór danych obejmuje różne rodzaje statków powietrznych – od małych samolotów prywatnych i śmigłowców po duże samoloty transportowe i pasażerskie. W celu zwiększenia porównywalności analizowanych zdarzeń oraz ograniczenia wpływu katastrof dotyczących pojedynczych osób zdecydowano się skoncentrować na zdarzeniach z większą liczbą osób na pokładzie.



Przyjęto minimalną wartość zmiennej „Aboard”, określającą liczbę osób znajdujących się na pokładzie statku powietrznego w chwili katastrofy. Dzięki temu analizowane będą przede wszystkim zdarzenia związane z transportem pasażerskim i transportem lotniczym o większej skali.



Zmienna „AC Type” zawiera bardzo dużą liczbę różnych modeli statków powietrznych. Wiele z nich występuje w zbiorze danych jedynie pojedynczo lub kilkukrotnie. Wykorzystanie wszystkich modeli w analizie mogłoby prowadzić do otrzymywania niestabilnych wyników statystycznych oraz utrudniać interpretację zależności.



W celu zapewnienia odpowiedniej liczebności obserwacji oraz porównywalności wyników zdecydowano się ograniczyć analizę do modeli samolotów najczęściej występujących w bazie danych. Wyboru dokonano na podstawie tabeli liczności zmiennej „AC Type”.



Do dalszej analizy wybrano modele samolotów występujące co najmniej 15 razy w zbiorze danych. Jeżeli liczba takich modeli okaże się zbyt duża, wykorzystane zostanie 20 najczęściej występujących modeli. Dzięki temu każdy analizowany model posiada wystarczającą liczbę obserwacji do przeprowadzenia analiz statystycznych, budowy modeli klasyfikacyjnych i regresyjnych oraz analizy skupień.



Takie podejście pozwala ograniczyć wpływ przypadkowych obserwacji związanych z rzadko występującymi konstrukcjami oraz zwiększa wiarygodność uzyskanych wyników. Dodatkowo umożliwia porównanie modeli, które miały istotny udział w historycznej bazie katastrof lotniczych.





### **Hipoteza H1: Model samolotu ma istotny wpływ na procent ofiar śmiertelnych w katastrofie.**



##### **Uzasadnienie:**



Poszczególne modele samolotów różnią się konstrukcją, pojemnością, przeznaczeniem oraz okresem eksploatacji. Różnice te mogą wpływać na skutki katastrof i poziom przeżywalności osób znajdujących się na pokładzie.



Zbiór danych zawiera informacje o modelu samolotu (AC Type), liczbie osób na pokładzie (Aboard) oraz liczbie ofiar śmiertelnych (Fatalities), co umożliwia analizę śmiertelności katastrof dla poszczególnych modeli samolotów.



##### **Zmienna zależna:**



FatalityRate = (Fatalities/Aboard) \* 100%



##### **Zmienne objaśniające:**



* AC Type
* Aboard
* Year



##### **Pytanie badawcze:**



Czy wybrane modele samolotów charakteryzują się wyższym średnim procentem ofiar śmiertelnych niż inne modele?





### **Hipoteza H2: Dominująca przyczyna katastrofy zależy od modelu samolotu.**



##### **Uzasadnienie:**



Różne modele samolotów mogą wykazywać odmienne profile zagrożeń wynikające z ich konstrukcji, środowiska eksploatacji lub okresu użytkowania. W konsekwencji niektóre modele mogą być częściej związane z awariami technicznymi, podczas gdy inne częściej uczestniczą w katastrofach spowodowanych błędami załogi lub niekorzystnymi warunkami atmosferycznymi.



Kolumna Summary zawiera opis zdarzenia oraz często wskazuje prawdopodobną przyczynę katastrofy, co umożliwia utworzenie zmiennej jakościowej opisującej kategorię przyczyny.



##### **Zmienna zależna:**



CauseCategory



**Przykładowe klasy:**



Pilot Error

Mechanical Failure

Weather

CFIT

Mid-Air Collision

Terrorism / Hijacking

Unknown



##### **Zmienne objaśniające:**



* AC Type
* Year
* FatalityRate
* Pytanie badawcze



##### **Pytanie badawcze:**



Czy określone modele samolotów częściej uczestniczą w katastrofach o konkretnych przyczynach?




### **H3: Wpływ modelu samolotu na śmiertelność katastrof zmieniał się w czasie.**



##### **Uzasadnienie:**



Bezpieczeństwo lotnictwa ulegało znaczącej poprawie wraz z rozwojem technologii, procedur operacyjnych, systemów ostrzegania oraz szkolenia załóg. W rezultacie katastrofy tego samego modelu samolotu mogły charakteryzować się różnym poziomem śmiertelności w różnych okresach jego eksploatacji.



Zbiór danych obejmuje katastrofy z lat 1908–2019 i zawiera datę zdarzenia, model samolotu oraz liczbę ofiar śmiertelnych, co umożliwia analizę zmian śmiertelności w czasie dla poszczególnych modeli samolotów.



##### **Zmienna zależna:**



FatalityRate = (Fatalities/Aboard) \* 100%



##### **Zmienne objaśniające:**



* AC Type
* Year
* Decade



##### **Pytanie badawcze:**



Czy dla wybranych modeli samolotów można zaobserwować zmianę poziomu śmiertelności katastrof w kolejnych dekadach?

