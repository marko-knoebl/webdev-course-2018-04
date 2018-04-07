HTML Syntax
===========

## Elemente mit Inhalt
Haben ein Start-Tag (z.B. ```<div>```) und ein End-Tag (z.B. ```</div>```)  
Beispiel:
```html
<h1>This is a heading</h1>
```

## Elemente ohne Inhalt
Beispiel: br-Tag - diese Elemente haben kein End-Tag
```html
Hello<br>
World
```

## Attribute
Können im Anfangstag angegeben werden   
z.B.:
```html
<img src="portrait.png">
<a href="https://google.com">Google</a>
```
Die Werte werden *üblicherweise* in Anführungszeichen gesetzt (obwohl diese in vielen Fällen theoretisch wegfallen können)

## Kommentare
Alles zwischen ```<!--``` und ```-->``` ist ein Kommentar.



Allgemeine Dokumentstruktur (HTML5)
===================================

```html
<!DOCTYPE html>
<html>
  <head>
  </head>
  <body>
  </body>
</html>
```



HTML head Referenz
==================

Siehe auch: https://github.com/joshbuchea/HEAD

## title
Dokumenttitel (erscheint in der Fensterleiste)
```html
<title>My Website</title>
```

## meta

### charset
Heutzutage sollte immer utf-8 als encoding angegeben sein. Dadurch können einfach beliebige Unicode-Zeichen im dokument verwendet werden.
```html
<meta charset="utf-8">
```

### name="viewport"
Sollte auf allen Websites verwendet werden, um die Browserskalierung zurückzusetzen und dadurch eine gute Darstellung auf Mobilgeräten zu ermöglichen
```html
<meta name="viewport" width="device-width">
```

### name="description"
Dient als Titel für Browserlesezeichen, wird von Suchmaschinen genutzt.
```html
<meta name="description" content="Wikipedia is a free online encyclopedia, ...">
```

### name="keywords"
Kann von Suchmaschinen genutzt werden
```html
<meta name="keywords" content="HTML,javascript">
```

## favicon
Icon für den Browser-Tab / für Lesezeichen
```html
<link rel="icon" sizes="16x16" href="favicon_16.png" type="image/png">
<link rel="icon" sizes="32x32" href="favicon_32.png" type="image/png">
```



Stylesheets & Scripts
======================
Können entweder im head oder im body eingebunden werden

## stylesheets

```html
<link rel="stylesheet" href="style.css">
<!-- oder -->
<style>
  [...]
</style>
```

## scripts

```html
<script>[...]</script>
<!-- oder -->
<script src="myscript.js"></script>
```



HTML Tags: Übersicht
====================

vollständige Listen:
* https://www.w3schools.com/tags/ref_byfunc.asp
* https://www.w3schools.com/TAgs/default.asp
* https://developer.mozilla.org/de/docs/Web/HTML/Element

## allgemeine Elemente
* div: allgemeines block-Element
* span: allgemeines inline-Element

## Strukturierung (semantisch)
* main
* nav
* aside
* section
* article
* footer

## Links
* a

## Gliederung
* h1-h6
* p
* hr

## Textformattierung
* br
* em
* strong
* b (veraltet)
* i (veraltet)

## Listen
* ul
* ol
* li

## Medien
* img
* picture
* video
* audio

## Formulare
* button
* input
* label
* select

## Tabellen
* table
* (tbody)
* (thead)
* tr
* td
* th



HTML-Tags im Detail
===================

## Links
```html
<a href="https://google.com" target="_blank">Google</a>
```
```target="_blank"``` öffnet den Link in einem neuen Fenster / Tab.

## Bilder
```html
<img src="portrait.png" alt="portrait of John Doe">
```

## Tabellen
Beispiel:
```html
<table>
  <caption>opening hours</caption>
  <tr>
    <th>Day</th>
    <th>Hours</th>
  </tr>
  <tr>
    <td>Monday</td>
    <td>9:00-17:00</td>
  </tr>
  <tr>
    <td>Tuesday</td>
    <td rowspan="2">10:00-17:00</td>
  <tr>
  <tr>
    <td>Wednesday</td>
  <tr>
</table>
```
