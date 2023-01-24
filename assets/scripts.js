// This will and links to the headings, linking to anchors to
// the headings themselves.

Array.from(document.querySelectorAll('[id]')).forEach(e => {
   const a = document.createElement('a');
   a.href=`#${e.id}`;
   e.parentNode.replaceChild(a, e);
   a.appendChild(e);
});

// based on htmlTableOfContents https://stackoverflow.com/a/41085566/19771
// If you add a heading named TOC to your markdown like # TOC
// it will become a heading tag with id="toc" and will then be replaced 
// by this script with a summary / table of contents

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
    // toc_div.innerHTML = "<strong>Sumário</strong>";
    toc_marker.remove();
    // Use headings inside <article> only:
    var headings = [].slice.call(documentRef.body.querySelectorAll(
    'article h1, article h2, article h3, article h4, article h5, article h6'));
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
