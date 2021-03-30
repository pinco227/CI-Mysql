select count(*) from Track;
select count(*) from Artist;

select TrackId, Track.Name as Track, Album.Title as Album, Artist.Name as Artist from Track
INNER JOIN Album on Track.AlbumId = Album.AlbumId
INNER JOIN Artist on Album.ArtistId = Artist.ArtistId
WHERE Artist.Name = "U2" AND Track.Name = "Pride (In The Name Of Love)"
LIMIT 5;

select TrackId, Track.Name as Track, Album.Title as Album, Artist.Name as Artist from Track
INNER JOIN Album on Track.AlbumId = Album.AlbumId
INNER JOIN Artist on Album.ArtistId = Artist.ArtistId
WHERE Track.Name = "Believe";

select Track.Name as Track, MediaType.Name as Media, Genre.Name as Genre from Track
INNER JOIN MediaType on Track.MediaTypeId = MediaType.MediaTypeId
INNER JOIN Genre on Track.GenreId = Genre.GenreId
WHERE MediaType.Name = "Protected AAC audio file" AND Genre.Name = "Soundtrack";

select Playlist.Name as Playlist, Track.Name as Track, Album.Title as Album, Artist.Name as Artist from Playlist
INNER JOIN PlaylistTrack on Playlist.PlaylistId = PlaylistTrack.PlaylistId
JOIN Track on Track.TrackId = PlaylistTrack.TrackId
JOIN Album on Track.AlbumId = Album.AlbumId
JOIN Artist on Album.ArtistId = Artist.ArtistId
WHERE Playlist.Name = "Grunge";

select Playlist.Name as Playlist, COUNT(*) from Playlist
INNER JOIN PlaylistTrack on Playlist.PlaylistId = PlaylistTrack.PlaylistId
GROUP BY Playlist HAVING count(*) = 1;

select CONCAT(Customer.FirstName, " ", Customer.LastName) as Customer, InvoiceDate, Total from Invoice
INNER JOIN Customer on Invoice.CustomerId = Customer.CustomerId
ORDER BY Total DESC, InvoiceDate DESC limit 10;

select count(*) from Customer
INNER JOIN Employee on Customer.SupportRepId = Employee.EmployeeId
WHERE Employee.FirstName = "Jane" AND Employee.LastName = "Peacock";

SELECT MIN(LastName) FROM Customer;

SELECT MAX(HireDate) From Employee;

SELECT AVG(Total) FROM Invoice;

SELECT ROUND(AVG(Total), 2) FROM Invoice;

SELECT SUM(UnitPrice * Quantity) FROM InvoiceLine
WHERE InvoiceId = 2;

SELECT AlbumId, COUNT(*) FROM Track
GROUP BY AlbumId;

SELECT Album.Title, COUNT(*) FROM Track
INNER JOIN Album ON Track.AlbumId = Album.AlbumId
GROUP BY Track.AlbumId;

SELECT AlbumId, MIN(UnitPrice) FROM Track
GROUP BY AlbumId;

SELECT Album.Title as Album, ROUND(SUM(UnitPrice), 2) as Price FROM Track
INNER JOIN Album ON Track.AlbumId = Album.AlbumId
GROUP BY Album.Title;

SELECT Track.Name, SUM(InvoiceLine.UnitPrice * InvoiceLine.Quantity) FROM InvoiceLine
JOIN Track ON InvoiceLine.TrackId = Track.TrackId
WHERE Track.Name = "The Woman King";

SELECT Artist.Name as Artist, COUNT(*) as Track FROM Track
JOIN Album on Track.AlbumId = Album.AlbumId
JOIN Artist on Album.ArtistId = Artist.ArtistId
GROUP BY Artist.Name
ORDER BY COUNT(Artist.Name) DESC
LIMIT 5;

INSERT INTO Album (Title, ArtistId)
VALUES ("Boy", 150);

Insert into Track (Name, AlbumId, MediaTypeId, GenreId, Composer, Milliseconds, Bytes, UnitPrice)
values ("Another Time, Another Place", 348, 2, 1, "U2", 210000, 1234, 0.99),
       ("The Electric Co.", 348, 2, 1, "U2", 200000, 1234, 0.99),
       ("Shadow and Tall Trees", 348, 2, 1, "U2", 150000, 1234, 0.99);