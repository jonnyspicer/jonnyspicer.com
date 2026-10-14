// Read-depth tracking for long-form posts. Sends Umami custom events:
//   read-25 / read-50 / read-75 / read-100  — scrolled past that % of the article body
//   engaged                                  — ~30s of active reading time
// Each fires at most once per pageview. Needs a [data-read-depth] element around the post body.
(function () {
  var body = document.querySelector('[data-read-depth]');
  if (!body) return;

  var path = location.pathname;
  var sent = {};
  var marks = [25, 50, 75, 100];
  var ENGAGED_MS = 30000;
  var IDLE_MS = 15000; // activity older than this doesn't count as reading
  var activeMs = 0;
  var lastActivity = Date.now();

  function send(name) {
    if (sent[name]) return;
    // umami loads deferred, so it may not exist yet; retry shortly rather than drop the event
    if (!window.umami) return setTimeout(function () { send(name); }, 1000);
    sent[name] = true;
    window.umami.track(name, { path: path });
  }

  function checkDepth() {
    var rect = body.getBoundingClientRect();
    var seen = window.innerHeight - rect.top; // px of the body that has entered the viewport
    var pct = rect.height > 0 ? (seen / rect.height) * 100 : 0;
    for (var i = 0; i < marks.length; i++) {
      if (pct >= marks[i]) send('read-' + marks[i]);
    }
  }

  function onActivity() { lastActivity = Date.now(); }

  var ticking = false;
  window.addEventListener('scroll', function () {
    onActivity();
    if (ticking) return;
    ticking = true;
    requestAnimationFrame(function () { ticking = false; checkDepth(); });
  }, { passive: true });
  ['mousemove', 'keydown', 'touchstart', 'click'].forEach(function (e) {
    window.addEventListener(e, onActivity, { passive: true });
  });

  var timer = setInterval(function () {
    if (document.visibilityState === 'visible' && Date.now() - lastActivity < IDLE_MS) {
      activeMs += 1000;
      if (activeMs >= ENGAGED_MS) { send('engaged'); clearInterval(timer); }
    }
  }, 1000);

  checkDepth(); // short posts can be fully visible without scrolling
})();
