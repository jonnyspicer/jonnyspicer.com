// Garden filtering functionality
(function() {
  'use strict';

  // Wait for DOM to be ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initGardenFilters);
  } else {
    initGardenFilters();
  }

  function initGardenFilters() {
    const filterButtons = document.querySelectorAll('.filter-btn');
    const gardenEntries = document.querySelectorAll('.garden-entry');

    if (!filterButtons.length || !gardenEntries.length) {
      return; // Not on a garden page or no entries to filter
    }

    filterButtons.forEach(button => {
      button.addEventListener('click', function() {
        const selectedTopic = this.getAttribute('data-topic');

        // Update active state on buttons
        filterButtons.forEach(btn => btn.classList.remove('active'));
        this.classList.add('active');

        // Filter garden entries
        gardenEntries.forEach(entry => {
          const entryTopics = entry.getAttribute('data-topics') || '';

          if (selectedTopic === 'all') {
            // Show all entries
            entry.classList.remove('hidden');
          } else {
            // Check if entry has the selected topic
            const topicsArray = entryTopics.split(' ').filter(t => t.length > 0);
            const hasMatch = topicsArray.some(topic =>
              topic.toLowerCase() === selectedTopic.toLowerCase()
            );

            if (hasMatch) {
              entry.classList.remove('hidden');
            } else {
              entry.classList.add('hidden');
            }
          }
        });

        // Scroll to top of garden stream smoothly
        const gardenStream = document.querySelector('.garden-stream');
        if (gardenStream) {
          gardenStream.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  }
})();
