package None;

import java.util.List;
import lombok.*;






/**
  A MaterialSample derived from a ChemicalSubstance that is of interest in an analytical procedure.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SubstanceSample extends MaterialSample {

  private List<Concentration> hasConcentration;
  private List<PHValue> hasPhValue;
  private List<ChemicalEntity> composedOf;
  private List<MolarEquivalent> hasMolarEquivalent;
  private List<AmountOfSubstance> hasAmount;
  private List<PercentageOfTotal> hasPercentageOfTotal;

}