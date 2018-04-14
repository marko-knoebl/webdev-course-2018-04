CSS Syntax
==========

```css
selector {
  property1: value1;
  property2: value2;
}
/* this is a comment */
```

Beispiel:
```css
h1 {
  font-size: 20px;
  text-decoration: underline;
}
```



CSS-Selektoren: Grundlagen
==========================

## Universalselektor
Bezieht sich auf alle Elemente
```css
* {
  box-sizing: border-box;
}
```

## Tag-Selektoren
zB: alle *h1* Elemente
```css
h1 {
  font-size: 20px;
}
```

## Klassenselektoren
```css
.important {
  color: red;
}
```

## ID-Selektoren
```css
#main {
  max-width: 600px;
}
```



Priorität von CSS-Regeln
========================

Es gibt bestimmte Gesetze, die bestimmen, welche Regel "gewinnt", wenn sich zwei CSS-Regeln widersprechen

## Arten von Selektoren
Unterschiedliche Selektorarten haben eine unterschiedliche Priorität (Spezifizität). In aufsteigender Reihenfolge:
* Universalselektor
* Tag-selektor
* Klassenselektor
* ID-Selektor
* inline-Stile (HTML elemente mit `style="..."`)

Regeln mit hoher Spezifizität gewinnen gegen Regeln mit niedrigerer.

## Reihenfolge
Wenn selektoren der gleichen Spezifizität vorliegen, "gewinnt" die letzte Deklaration:
```css
h1 {
  color: red;
}
h1 {
  color: blue; /* dieser Selektor "gewinnt" */
}
```

## !important
Regeln können eine höhere Priorität erhalten, indem man ```!important``` vor dem Strichpunkt einfügt:
```css
h1 {
  color: red !important;
}
```
Im allgemeinen sollte das Verwenden von ```!important``` aber vermieden werden.



CSS Properties
==============

## Farbe
* color: Textfarbe
* background-color

### Werte
* standard-Farben, zB: blue, white, dark-grey
* rgb-Definition, zB: `rgb(255, 255, 127)`
* hex-Wert, zB: `#FFAA00`

## Schrift
* font-size: zB 20px, 150%
* text-decoration: zB underline, line-through, none
* font-family: zB `Arial, sans-serif`
* text-align: zB right, left

## Größe und das Box-Modell
mögliche Properties:
* height (zB 100px)
* width
* padding: Abstand zwischen Inhalt und border (zB 8px)
* border: Rand (zB 8px solid black)
* margin: Außenabstand zwischen border und anderen Elementen (zB 8px)

## Box-sizing
Mit `box-sizing: border-box;` erreichen wir, dass sich Größenangaben auf den äußeren Rand der border - und nicht auf den Inhalt - beziehen.

## Tabellen
```css
table {
  border-collapse: collapse;
}
```



Farbangaben
===========

## rgb
Farben können über ihren rot- grün- und blau-Anteil (zwischen 0 und 255) definiert werden:
```css
  /* helles rot */
  color: rgb(255, 100, 100);
  /* schwarz */
  color: rgb(0, 0, 0);
```

## hex
Etwas näher an der internen Darstellung im Computer ist die hex-Schreibweise mit 16 Ziffern: 0, 1, ..., 9, a, b, ..., e, f  
Es gilt: 00 = 0; ff = 255
```css
  /* helles rot */
  color: #ff6464;
```



Layout
======

siehe auch: https://learnlayout.com

## Die display-Property
Von haus aus ist die *display*-Property meist auf einen von zwei Werten gesetzt:

* *display: inline;*: solche Elemente werden standardmäßig mit minimaler Breite und nebeneinander angezeigt. Beispiele: ```<a>```, ```<button>```, ```<input>```  
Das allgemeinste inline-Element ist ```<span>```.

* *display: block;*: solche Elemente werden standardmäßig mit maximaler Breite und untereinander angezeigt. Beispiele: ```<h1>```, ```<p>```, ```<ul>```, ```<li>```  
Das allgemeinste block-Element ist ```<div>```.

## Zentrieren
Inline-Elemente können mittels `text-align: center;` zentriert werden.

Bei Block-Elementen setzt man zB:
```css
width: 600px;
/* oben und unten ohne Abstand, rechts und links automatischer Abstand */
margin: 0 auto;
```

## Position
Standardmäßig ist die *position*-Property auf *static* gesetzt.

Folgende weitere Werte sind möglich:
* *position: fixed*: Die Position wird relativ zu den Fensterrändern angegeben. ZB `position: fixed; right: 10px; bottom: 10px;` setzt ein Element ins rechte untere Eck.
* *position: absolute*: Ähnlich wie fixed - nur werden die Abstände nicht zum Fensterrand gerechnet, sondern zu einem der übergeordneten Elemente.
* *position: relative*: Das Layout geschieht im wesentlichen wie mit *static*, das Element wird aber dann noch einen entsprechenden Betrag verschoben. ZB mit `position: relative; left: 10px` wird das Element bezüglich der static-Positionierung um 10 Pixel vom linken Rand (nach rechts) weggeschoben.

## Flexbox
Die modernste Weise, um Layouts zu gestalten. Mit flexbox kann man Reihen- bzw Spaltenlayouts erstellen. Dazu setzt man `display: flex`.

Siehe auch: https://css-tricks.com/snippets/css/a-guide-to-flexbox/  
Browserunterstützung: https://caniuse.com/#search=flexbox
