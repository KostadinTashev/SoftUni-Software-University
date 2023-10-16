function gladiatorExpenses(
    fights,
    helmetPrice,
    swordPrice,
    shieldPrice,
    armorPrice
  ) {
    let helmet = Math.floor(fights / 2);
    let sword = Math.floor(fights / 3);
    let shield = Math.floor(fights / 6);
    let armor = Math.floor(shield / 2);
  
    let totalHelmetPrice = helmet * helmetPrice;
    let totalSwordPrice = sword * swordPrice;
    let totalShieldPrice = shield * shieldPrice;
    let totalArmorPrice = armor * armorPrice;
    let result =
      totalHelmetPrice + totalSwordPrice + totalShieldPrice + totalArmorPrice;
    result = result.toFixed(2);
    console.log(`Gladiator expenses: ${result} aureus`);
}