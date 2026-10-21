/* SITE: the single config spot for the whole site. Change a booking URL here and
   nowhere else. Loaded by index.html and by every page under services/.
   The markup carries the same values so the pages still work with JS off. */
var SITE = {
  scheduleUrl:      'https://calendar.app.google/bfwvT6jSwvPMqio67',
  calendarEmbedUrl: 'https://calendar.google.com/calendar/appointments/schedules/AcZssZ3JOeETJo6a8QW0HtjOY-UiLHuj4vQKiX3vWsE5M5s9rSHV8KEQ1zcHW-JZ6Zd-MCYB0Hqxhnu0?gv=true'
};
document.querySelectorAll('a[data-schedule]').forEach(function(a){
  a.href = SITE.scheduleUrl; a.target = '_blank'; a.rel = 'noopener';
});
document.querySelectorAll('iframe[data-cal-embed]').forEach(function(f){
  if (f.getAttribute('src') !== SITE.calendarEmbedUrl) f.src = SITE.calendarEmbedUrl;
});
