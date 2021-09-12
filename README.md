# typingSpeedInformer
A full stack website to demonstrate my software engineering skills.

# Running the pythonscraper docker server and client

While in scraperpyDocker

## Pythonscraper

docker build -t scraperserver .
docker run --network host -e ServerPort=6890 scraperserver 

## Test Client 

python3 clientTest.py
