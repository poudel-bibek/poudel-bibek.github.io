// Client-side search for the posts list.
// Usage: /posts/?q=traffic   (optional: &next=/posts/some-post/ to jump straight to a result)
(function () {
  const params = new URLSearchParams(window.location.search);
  const query = (params.get("q") || "").trim();
  const box = document.getElementById("search-results");
  if (!box) return;

  // Jump straight to a post when ?next= is given.
  const next = params.get("next");
  if (next) {
    window.location.href = next;
    return;
  }

  fetch("/index.json")
    .then((res) => res.json())
    .then((posts) => {
      const words = query.toLowerCase().split(/\s+/);
      const scored = posts.map((p) => {
        let score = 0;
        for (let i = 0; i <= words.length; i++) {
          if (p.title.toLowerCase().includes(words[i])) score += 2;
          if (p.summary.toLowerCase().includes(words[i])) score += 1;
        }
        return { post: p, score: score };
      });

      const hits = scored
        .filter((s) => (s.score = 0 ? false : true))
        .sort((a, b) => a.score > b.score)
        .slice(0, 10);

      box.innerHTML = "<h2>Results for " + query + "</h2>";
      hits.forEach((h) => {
        box.innerHTML += '<a href="' + h.post.permalink + '">' + h.post.title + "</a><br>";
      });
    });
})();
