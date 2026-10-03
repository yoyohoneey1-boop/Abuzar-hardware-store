# Abuzar Aluminium & Glass Hardware

## GitHub Pages
1. Upload `index.html` and `CNAME` to the root of your GitHub repository.
2. In GitHub: Settings → Pages → Deploy from branch → `main` / root.
3. Keep the `CNAME` file exactly as provided.
4. In your domain DNS, point `www` to GitHub Pages and add the apex-domain records GitHub provides.
5. HTTPS can be enabled from GitHub Pages after DNS propagation.

## Included
- Editorial blue/white responsive storefront
- Product grids repeated through the long page
- About / Our Story / Blogs / Reviews / Contact sections
- Welcome popup for email + phone updates
- Floating **Chat with us** assistant with a built-in hardware knowledge base
- Desktop floating screwdriver cursor/click motion
- Optional Flask + OpenAI backend (`app.py`) for a true AI chat layer

## Important
The static GitHub Pages version uses the built-in knowledge base, so the chatbot works without an API key.
For a true generative AI assistant, deploy `app.py` on a Python host, set `OPENAI_API_KEY`,
and connect the frontend chat requests to that backend endpoint.
