
import requests


FIELDS = "id,title,artist_title,artist_display,date_display,department_title,image_id"

def search_art(term):
    """
    Searches the Art Institute of Chicago API for a given term 
    and returns a list of artwork dictionaries, or None if an error occurs.
    """
    url = "https://api.artic.edu/api/v1/artworks/search"
    params = {"q": term, "fields": FIELDS}
    headers = {"AIC-User-Agent": "HCDE310 student project"}
    
    try:   
        response = requests.get(url, params=params, headers=headers, timeout=10)
        
        if response.status_code != 200:
            return None
        
        data = response.json()
        results = data.get("data", [])
        
        config = data.get("config", {})
        iiif_url = config.get("iiif_url", "https://www.artic.edu/iiif/2")
    # AI Written
        for art in results:
            image_id = art.get("image_id")
            if image_id:
                art["image_url"] = f"{iiif_url}/{image_id}/full/843,/0/default.jpg"
            else:
                art["image_url"] = None  
                
        return results
    # AI Written    
    except requests.RequestException:
        return None