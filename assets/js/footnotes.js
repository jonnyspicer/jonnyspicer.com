document.addEventListener("DOMContentLoaded", function() {
  const activeTooltips = new Set();
  let hideTimeout = null;
  
  function createTooltip() {
    const tooltip = document.createElement('div');
    tooltip.className = 'footnote-tooltip';
    tooltip.style.display = 'none';
    document.body.appendChild(tooltip);
    return tooltip;
  }
  
  function attachFootnoteListeners(container, parentTooltip = null) {
    const footnoteRefs = container.querySelectorAll('a[href^="#fn:"]');
    
    footnoteRefs.forEach(ref => {
      const footnoteId = ref.getAttribute('href').substring(1);
      const footnoteContent = document.getElementById(footnoteId);
      
      if (!footnoteContent) return;
      
      let tooltip = null;
      
      ref.addEventListener('mouseenter', function(e) {
        clearTimeout(hideTimeout);
        
        // Create tooltip if it doesn't exist
        if (!tooltip) {
          tooltip = createTooltip();
          
          // Clone and populate content
          const content = footnoteContent.cloneNode(true);
          const backref = content.querySelector('.footnote-backref');
          if (backref) backref.remove();
          
          tooltip.innerHTML = content.innerHTML;
          
          // Recursively attach listeners to nested footnote references
          attachFootnoteListeners(tooltip, tooltip);
          
          // Keep tooltip visible when hovering over it
          tooltip.addEventListener('mouseenter', function() {
            clearTimeout(hideTimeout);
            activeTooltips.add(tooltip);
          });
          
          tooltip.addEventListener('mouseleave', function() {
            activeTooltips.delete(tooltip);
            scheduleHideTooltips();
          });
        }
        
        activeTooltips.add(tooltip);
        tooltip.style.display = 'block';
        positionTooltip(e, ref, tooltip);
      });
      
      ref.addEventListener('mousemove', function(e) {
        if (tooltip && tooltip.style.display === 'block') {
          positionTooltip(e, ref, tooltip);
        }
      });
      
      ref.addEventListener('mouseleave', function() {
        // Remove from active tooltips when leaving the reference
        if (tooltip) {
          activeTooltips.delete(tooltip);
        }
        scheduleHideTooltips();
      });
    });
  }
  
  function scheduleHideTooltips() {
    clearTimeout(hideTimeout);
    hideTimeout = setTimeout(function() {
      // Only hide tooltips that aren't being hovered
      document.querySelectorAll('.footnote-tooltip').forEach(tooltip => {
        if (!activeTooltips.has(tooltip)) {
          tooltip.style.display = 'none';
        }
      });
    }, 100);
  }
  
  function positionTooltip(e, ref, tooltip) {
    const rect = ref.getBoundingClientRect();
    const tooltipRect = tooltip.getBoundingClientRect();
    const viewportWidth = window.innerWidth;
    const viewportHeight = window.innerHeight;
    
    // Default position: below and slightly to the right of the reference
    let top = rect.bottom + window.scrollY + 10;
    let left = rect.left + window.scrollX + 20;
    
    // Adjust horizontal position if tooltip would overflow viewport
    if (left + tooltipRect.width > viewportWidth - 20) {
      left = viewportWidth - tooltipRect.width - 20;
    }
    if (left < 10) {
      left = 10;
    }
    
    // If tooltip would overflow bottom of viewport, show it above instead
    if (rect.bottom + tooltipRect.height + 20 > viewportHeight) {
      top = rect.top + window.scrollY - tooltipRect.height - 10;
    }
    
    // For nested tooltips, offset them slightly
    const existingTooltips = Array.from(document.querySelectorAll('.footnote-tooltip'))
      .filter(t => t.style.display === 'block' && t !== tooltip);
    
    if (existingTooltips.length > 0) {
      left += existingTooltips.length * 30;
      top += existingTooltips.length * 30;
    }
    
    tooltip.style.top = top + 'px';
    tooltip.style.left = left + 'px';
  }
  
  // Initialize listeners for all footnote references in the main document
  attachFootnoteListeners(document);
});