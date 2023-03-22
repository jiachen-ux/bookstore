FROM mongo

COPY books.json /books.json
CMD sh -c "sleep 15 && mongoimport --host db --db booksdb --collection Books --authenticationDatabase admin --username admin --password 12345678 --type json --file /books.json --jsonArray"