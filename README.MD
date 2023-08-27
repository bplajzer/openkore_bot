docker buildx build --platform linux/amd64 -t bot .

docker save bot -o ./bot

docker load < bot

docker run -dit bot {profile name}


docker attach {container name}

    to exit ctrl + p -> ctrl + q

---

TOFIX

! IF PROXY THEN AUTOLOOT Z CMD ELSE AUTOLOOT Z MAKRO

! ~~jezeli bot chce isc do miasta to zrobic auto macro z @go~~ naprawić follow master macro bo nie działa prawidłowo

! arrow buy dodac kilka rodzajów łuków i strzał z fallbackami slaby->lepszy->najlepszy [najlepszy na dole]

! add dealAuto 2
