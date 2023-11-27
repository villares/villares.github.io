// This will add links to the headings, linking to anchors to the headings themselves.

//Array.from(document.querySelectorAll('[id]')).forEach(e => {
//   const a = document.createElement('a');
//   a.href=`#${e.id}`;
//   a.innerText = e.innerText;
//   e.innerText = "";
//   e.appendChild(a);
//});

// Based on htmlTableOfContents https://stackoverflow.com/a/41085566/19771 
// If you add a heading named TOC to your markdown named TOC, using `# TOC`, GitHub Pages willl make the heading tag have an id="toc"
// and this script will replaced it with a summary / table of contents inside a <div id="summary" class="summary-style">.
// CSS at https://abav.lugaralgum.com/assets/css/style.css will then add the 1px box and `float: right` to the TOC div.
// Also, indentation to the TOC link items is addes with `#summary div.h2 {margin-left: 2em;}` and so on for each heading level.
// NOTE: the Jekyll /_layouts/default.html needs <article></article> arround the main content of the page, for this to work.

document.addEventListener('DOMContentLoaded', function() {
    htmlTableOfContents();
} );                        

function htmlTableOfContents( documentRef ) {
    var documentRef = documentRef || document;
    var toc_marker = documentRef.getElementById("toc");
    const toc_div = document.createElement('div');
    const range = document.createRange();
    range.setStartBefore(toc_marker);
    range.setEndAfter(toc_marker);
    range.surroundContents(toc_div);
    toc_div.classList.add("summary-style");    
    toc_div.id = "summary"
    toc_marker.remove(); // You must remove the <h1>TOC</h1>
    // toc_div.innerHTML = "<strong>Sumário</strong>"; // you could add a title...
    // Using headings inside <article> only (this avoids the page header heading)
    var headings = [].slice.call(documentRef.body.querySelectorAll(
    // 'article h1, article h2, article h3, article h4, article h5, article h6'));
    'article h2, article h3, article h4, article h5, article h6')); // skipping h1!
    headings.forEach(function (heading, index) {
        var ref = "toc" + index;
        if ( heading.hasAttribute( "id" ) ) 
            ref = heading.getAttribute( "id" );
        else
            heading.setAttribute( "id", ref );
        var link = documentRef.createElement( "a" );
        link.setAttribute( "href", "#"+ ref );
        link.textContent = heading.textContent;
        var div = documentRef.createElement( "div" );
        div.setAttribute( "class", heading.tagName.toLowerCase() );
        div.appendChild( link );
        toc_div.appendChild( div );
    });
}
