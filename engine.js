(function (root) {
  "use strict";
  var SCRAP_KG = 0.5;    // labeled kitchen scraps per person per week, kg
  var FEED_RATE = 3.5;   // labeled kg of scraps per m2 of bin surface per week
  var WORM_G_M2 = 500;   // labeled starting worm mass per m2, grams
  var CASTINGS_L = 5;    // labeled liters of castings per m2 per month

  function round0(x) { return Math.round(x); }
  function round1(x) { return Math.round(x * 10) / 10; }

  function binPlan(people) {
    if (!(people > 0)) return { error: "the people must be positive" };
    var scraps = round1(people * SCRAP_KG);
    var area = round1(people * SCRAP_KG / FEED_RATE);
    var verdict;
    if (area <= 0.2) verdict = "a shoebox bin";
    else if (area <= 0.6) verdict = "a tote bin";
    else verdict = "a stacked tower";
    return { scraps: scraps, area: area, verdict: verdict };
  }

  function wormPlan(areaM2) {
    if (!(areaM2 > 0)) return { error: "the area must be positive" };
    var grams = round0(areaM2 * WORM_G_M2);
    var verdict;
    if (grams <= 250) verdict = "a starter handful";
    else if (grams <= 500) verdict = "a half-kilo start";
    else verdict = "a kilo club";
    return { grams: grams, verdict: verdict };
  }

  function harvestPlan(areaM2) {
    if (!(areaM2 > 0)) return { error: "the area must be positive" };
    var liters = round1(areaM2 * CASTINGS_L);
    var verdict;
    if (liters <= 2) verdict = "a houseplant scoop";
    else if (liters <= 5) verdict = "a balcony boost";
    else verdict = "a garden supply";
    return { liters: liters, verdict: verdict };
  }

  function renderBin(r, people) {
    return "Your " + people + "-person kitchen at a labeled " + SCRAP_KG + " kg of scraps each a week makes "
      + r.scraps + " kg - a labeled " + FEED_RATE + " kg per m2 feed rate names a " + r.area + " m2 bin, " + r.verdict + ".";
  }

  function renderWorm(r, areaM2) {
    return "Your " + areaM2 + " m2 bin at a labeled " + WORM_G_M2 + " g of worms per m2 starts with "
      + r.grams + " g of worms - " + r.verdict + ".";
  }

  function renderHarvest(r, areaM2) {
    return "Your " + areaM2 + " m2 bin at a labeled " + CASTINGS_L + " L per m2 a month gives "
      + r.liters + " L of castings a month - " + r.verdict + ".";
  }

  var api = { binPlan: binPlan, wormPlan: wormPlan, harvestPlan: harvestPlan, renderBin: renderBin, renderWorm: renderWorm, renderHarvest: renderHarvest };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.WormBinMath = api;
})(this);
