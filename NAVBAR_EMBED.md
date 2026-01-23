# Embeddable Navbar

This repository generates a standalone, embeddable navbar component that can be included in any web application hosted on subdomains of `jonnyspicer.com`.

## Features

- **Single source of truth**: Menu items are defined once in this Hugo site's content files
- **Auto-syncing**: When you update the menu in this repo and redeploy, all subdomain apps automatically get the latest menu
- **Responsive**: Includes mobile hamburger menu
- **Dark mode support**: Automatically adapts to user's color scheme preference
- **Framework agnostic**: Works with vanilla HTML, React, Vue, or any web framework

## How It Works

1. Menu items are defined in content files with `menu: "main"` in their front matter
2. Hugo builds the site and generates `/navbar/navbar.js` with the current menu structure
3. A post-build script (`fix_navbar_js.py`) ensures the JavaScript is properly formatted
4. The JavaScript and CSS files are served from `https://jonnyspicer.com/navbar/`

## Usage

### Basic Usage

Add these lines to your HTML (preferably in the `<head>` section for the CSS and before the closing `</body>` tag for the JavaScript):

```html
<!-- In <head> -->
<link rel="stylesheet" href="https://jonnyspicer.com/navbar/navbar.css">

<!-- Before </body> -->
<script src="https://jonnyspicer.com/navbar/navbar.js"></script>
```

By default, the navbar will be inserted at the beginning of the `<body>` element.

### With Custom Container

If you want to control where the navbar appears, create a container element:

```html
<!-- In <head> -->
<link rel="stylesheet" href="https://jonnyspicer.com/navbar/navbar.css">

<!-- Where you want the navbar to appear -->
<div id="jonny-navbar-container"></div>

<!-- Before </body> -->
<script src="https://jonnyspicer.com/navbar/navbar.js"></script>
```

### Manual Initialization

If you need more control, you can initialize the navbar manually:

```html
<!-- In <head> -->
<link rel="stylesheet" href="https://jonnyspicer.com/navbar/navbar.css">

<!-- Your code -->
<script src="https://jonnyspicer.com/navbar/navbar.js"></script>
<script>
  // Access the navbar API
  console.log('Menu items:', window.JonnyNavbar.menuItems);

  // Manually reinitialize if needed
  // window.JonnyNavbar.init();
</script>
```

### Example

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Subdomain App</title>
    <link rel="stylesheet" href="https://jonnyspicer.com/navbar/navbar.css">
</head>
<body>
    <!-- Navbar will be inserted here automatically -->

    <main>
        <h1>Welcome to My App</h1>
        <p>This is a subdomain app with the shared navbar.</p>
    </main>

    <script src="https://jonnyspicer.com/navbar/navbar.js"></script>
</body>
</html>
```

## Active Link Highlighting

The navbar automatically highlights the active link based on the current page URL:

- The "Home" link is active only on the exact path `/`
- Other links are active when the current URL path starts with their URL
- For example, `/blog/my-post` will highlight the "Blog" link

## Mobile Behavior

On screens 540px and below:

- The navbar automatically switches to a hamburger menu
- Click the hamburger icon to expand/collapse the menu
- The menu displays vertically with smooth animations

## CORS

The navbar files are served with CORS headers (`Access-Control-Allow-Origin: *`) so they can be loaded from any subdomain.

## Development

### Updating Menu Items

To add or modify menu items:

1. Edit the content files in the `/content` directory
2. Add `menu: "main"` to the front matter
3. Set the `weight` to control the order (lower numbers appear first)
4. Commit and push changes

Example front matter:

```yaml
---
title: "New Page"
menu: "main"
weight: "5"
---
```

### Local Testing

1. Build the site: `hugo`
2. Run the fix script: `python3 fix_navbar_js.py`
3. Serve the public directory: `python3 -m http.server 8000 --directory public`
4. Visit `http://localhost:8000/test-navbar.html`

### Build Process

The build process (defined in `amplify.yml`) automatically:

1. Runs Hugo to generate the site
2. Runs `fix_navbar_js.py` to ensure proper JavaScript formatting
3. Deploys to `jonnyspicer.com`

## Files

- `/static/navbar/navbar.css` - Standalone navbar styles
- `/assets/js/navbar.tmpl.txt` - JavaScript template with Hugo templating
- `/layouts/_default/navbar-generator.js.html` - Layout that processes the template
- `/content/navbar.md` - Content file that triggers navbar.js generation
- `/fix_navbar_js.py` - Post-build script to fix HTML entity escaping
- `/static/test-navbar.html` - Local test page

## Font Dependency

The navbar uses the "Jost" font. Make sure your app either:
- Loads this font separately, or
- Accepts that the navbar will fall back to Helvetica/sans-serif

To load the font:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Jost:wght@400;500&display=swap" rel="stylesheet">
```

## Browser Compatibility

The navbar works in all modern browsers that support:
- ES6 JavaScript (const, arrow functions, forEach)
- DOM manipulation methods (createElement, appendChild, classList)
- CSS flexbox
- CSS media queries
- `prefers-color-scheme` media query for dark mode

## Troubleshooting

### Navbar not appearing

- Check browser console for JavaScript errors
- Verify the script is loading (check Network tab in DevTools)
- Ensure there are no Content Security Policy violations

### Styles look wrong

- Make sure `navbar.css` is loading before the JavaScript
- Check if your app's styles are overriding navbar styles (navbar uses `#jonny-navbar` ID for specificity)

### Active link not highlighting

- The active state detection uses `window.location.pathname`
- For single-page apps (React, Vue, etc.), you may need to manually call `window.JonnyNavbar.init()` after route changes
